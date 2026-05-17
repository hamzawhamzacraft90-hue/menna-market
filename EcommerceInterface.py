import streamlit as st
import mysql.connector
import pandas as pd

# 1. إعدادات الصفحة الاحترافية (Dark Mode فخم جداً)
st.set_page_config(page_title="MENNA BEH MARKET - لوحة التحكم الرقمية", page_icon="🟢", layout="wide")

# 2. حقن ستايل الـ Dark Cyber-WhatsApp الحديث والمبهر جداً
dark_modern_style = """
<style>
    /* تغيير الخلفية البيضاء المعفنة لأسود داكن فخم جدًا */
    .stApp {
        background-color: #0B141A !important;
        color: #E9EDEF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* الهيدر العلوي الذكي (Top Bar) */
    .main-header {
        background: linear-gradient(135deg, #128C7E 0%, #075E54 100%);
        padding: 25px;
        border-bottom: 2px solid #00A884;
        margin-bottom: 35px;
        text-align: center;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 168, 132, 0.2);
    }
    
    /* صناديق كروت الإحصائيات (Glassmorphism Metrics) */
    [data-testid="metric-container"] {
        background-color: #111B21 !important;
        border: 1px solid #222E35 !important;
        border-top: 4px solid #00A884 !important; /* نيون أخضر مضيء */
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* نصوص الإحصائيات داخل الكروت */
    [data-testid="stMetricLabel"] {
        color: #8696A0 !important;
        font-size: 0.95rem !important;
    }
    [data-testid="stMetricValue"] {
        color: #00A884 !important;
        font-size: 1.8rem !important;
        font-weight: bold !important;
    }
    
    /* الأزرار الانسيابية السلسة بمؤثرات حركية خرافية */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00A884 0%, #25D366 100%) !important;
        color: #111B21 !important;
        border-radius: 30px !important;
        border: none !important;
        font-weight: 800 !important;
        padding: 12px 35px;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 168, 132, 0.4);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #25D366 0%, #00A884 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(37, 211, 102, 0.6);
    }

    /* شريط التبويبات (Tabs) بشكل مذهل ونظيف */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #111B21 !important;
        padding: 8px !important;
        border-radius: 12px !important;
        border: 1px solid #222E35;
    }
    .stTabs [data-baseweb="tab"] {
        color: #8696A0 !important;
        font-weight: 600 !important;
        padding: 14px 40px !important;
        transition: 0.2s;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00A884 !important;
        color: #111B21 !important;
        border-radius: 8px !important;
        font-weight: bold !important;
    }
    
    /* حقول الإدخال والقوائم */
    input, select, div[data-baseweb="select"], .stNumberInput input, .stTextInput input {
        background-color: #222E35 !important;
        color: #E9EDEF !important;
        border-radius: 12px !important;
        border: 1px solid #323D45 !important;
        padding: 10px !important;
    }
    input:focus {
        border-color: #00A884 !important;
    }
    
    /* الجداول الذكية الاحترافية */
    div[data-testid="stDataFrame"] {
        background-color: #111B21 !important;
        border: 1px solid #222E35 !important;
        border-radius: 15px !important;
        padding: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.4);
    }
    
    /* الخطوط الفاصلة */
    hr {
        border-color: #222E35 !important;
    }
</style>
"""
st.markdown(dark_modern_style, unsafe_allow_html=True)

# 3. الاتصال بقاعدة البيانات (مع الاحتفاظ بالباسورد hamza)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root", 
        password="hamza",  
        database="E_commerce_System"
    )

# 4. دالة التغذية التلقائية لحل مشكلة "الموقع فاضي" نهائياً
def auto_seed_market(cursor, conn):
    cursor.execute("SELECT COUNT(*) FROM Product")
    if cursor.fetchone()[0] == 0:
        products = [
            (201, 'كيس شيبسي عائلي طماطم', 10.00), (202, 'مولتو ماجنم شوكولاتة', 15.00),
            (203, 'علبة لبن جهينة كامل الدسم 1 لتر', 48.00), (204, 'باكو شاي العروسة ربع كيلو', 70.00),
            (205, 'كيس أندومي فراخ خارق', 10.00), (206, 'كانز شويبس رمان ساقع', 15.00),
            (207, 'كانز فيروز تفاح روقان', 13.00), (208, 'علبة جبنة دومتي فيتا نص كيلو', 45.00),
            (209, 'زجاجة زيت كريستال عباد 1 لتر', 95.00), (210, 'كيس أرز الضحى فاخر 1 كيلو', 42.00),
            (211, 'برطمان مربى فيتراك فراولة', 40.00), (212, 'برطمان نسكافيه بلاك صغير', 65.00),
            (213, 'باكو بسكويت أولكر شمعدان', 7.00), (214, 'صاروخ بيبسي بلاستيك 1.5 لتر', 27.00),
            (215, 'كانز ماكس كولا ساقع أصلي', 12.00), (216, 'عصير تويست مانجو طبيعي مراق', 10.00),
            (217, 'مشروب طاقة فيوري باور مصري', 25.00), (218, 'باكت نسكافيه بلاك مصر فرط', 5.00),
            (219, 'شوكولاتة نسكافيه بريك مقرمشة', 15.00), (220, 'كيس أندومي خضار بالليمون الشهير', 10.00),
            (221, 'علبة حليب ميكس شوكولاتة جهينة سناك', 15.00), (222, 'زجاجة سبيرو سباتس دبل ترويق', 10.00),
            (223, 'قالب جبنة قريش فلاحي أصلي من ماركت يمنى', 250.00)
        ]
        cursor.executemany("INSERT INTO Product (productID, PName, Price) VALUES (%s, %s, %s)", products)
        conn.commit()

# الهيدر الفخم المطور لـ YOUMNA MARKET
st.markdown("<div class='main-header'><h1 style='color: #FFFFFF; font-weight:900; letter-spacing: 2px; margin:0;'>🟢 YOUMNA MARKET</h1><p style='color: #00A884; font-weight:600; margin:5px 0 0 0;'>ENTERPRISE MANAGEMENT SYSTEM</p></div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📋 لوحة التحكم الرقمية", "➕ إضافة صنف جديد"])

# --- القسم الأول: عرض المنتجات الذكي والإحصائيات الحية ---
with tab1:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # تشغيل التغذية التلقائية فوراً لو كان الجدول فارغ
        auto_seed_market(cursor, conn)
        
        cursor.execute("SELECT * FROM Product")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        
        if rows:
            df = pd.DataFrame(rows, columns=columns)
            id_col = df.columns[0] 
            
            # عرض الكروت الرقمية الفخمة
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="📊 أعلى قيمة صنف مخزون", value=f"{df['Price'].max()} ج.م")
            with col2:
                st.metric(label="📊 الصنف الأكثر اقتصاداً", value=f"{df['Price'].min()} ج.م")
            with col3:
                st.metric(label="📊 إجمالي وحدات السلع المتاحة", value=f"{len(df)} صنف")
            
            st.write("---")
            
            st.markdown("<h4 style='color: #00A884;'>🔍 الفلترة والبحث الفوري عن السلع</h4>", unsafe_allow_html=True)
            search_query = st.text_input("ادخل اسم السلعة المطلوبة للبحث المباشر:", placeholder="مثال: ماكس كولا، أندومي، جبنة...")
            
            if search_query:
                filtered_df = df[df['PName'].str.contains(search_query, case=False, na=False)]
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.dataframe(df, use_container_width=True)
                
            st.write("---")
            
            # حذف منتج واحد
            st.markdown("<h4 style='color: #00A884;'>🗑️ سحب وإهلاك صنف من المخزن</h4>", unsafe_allow_html=True)
            product_to_delete = st.selectbox("حدد كود الصنف المراد تصفيته نهائياً:", df[id_col].tolist())
            if st.button("🔴 إهلاك الصنف المحدد فوراً"):
                try:
                    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
                    cursor.execute("DELETE FROM review WHERE product_id = %s", (product_to_delete,))
                    cursor.execute("DELETE FROM Product WHERE productID = %s", (product_to_delete,))
                    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
                    conn.commit()
                    st.error(f"⚠️ تم مسح وإهلاك الصنف رقم ({product_to_delete}) بنجاح!")
                    st.rerun()
                except Exception as ex:
                    st.error(f"خطأ أثناء المسح: {ex}")
                
            st.write("---")
            
            # زر التصفير الشامل الاحترافي
            st.markdown("<h4 style='color: #FF2E74;'>🚨 تصفير وإخلاء المخازن بالكامل</h4>", unsafe_allow_html=True)
            if st.button("💥 تدمير السجلات وتصفير الرفوف"):
                st.session_state['confirm_delete_all'] = True
                
            if st.session_state.get('confirm_delete_all', False):
                st.error("❗ تأكيد نهائي: سيتم إخلاء الماركت بالكامل. هل تريد الاستمرار؟")
                col_yes, col_no = st.columns([1, 10])
                with col_yes:
                    if st.button("✅ تأكيد الإخلاء"):
                        try:
                            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
                            cursor.execute("TRUNCATE TABLE review")    
                            cursor.execute("TRUNCATE TABLE Product")   
                            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
                            conn.commit()
                            st.session_state['confirm_delete_all'] = False
                            st.success("💥 تم تصفير المخازن بنجاح!")
                            st.rerun()
                        except Exception as ex:
                            st.error(f"فشلت العملية: {ex}")
                
        else:
            st.info("نظام المخازن فارغ تماماً حالياً.")
            
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"خطأ اتصال بالنظام الرئيسي: {e}")

# --- القسم الثاني: إضافة السلع الجديدة للمخزون ---
with tab2:
    st.markdown("<h3 style='color: #00A884;'>⚡ تسجيل صنف تجاري جديد</h3>", unsafe_allow_html=True)
    with st.form("market_add_form"):
        p_id = st.number_input("كود السلعة الفريد (ID)", min_value=1, step=1)
        p_name = st.text_input("الاسم التجاري للسلعة (Name)", placeholder="مثال: علبة حليب ميكس شوكولاتة جهينة")
        p_price = st.number_input("سعر التوريد المعتمد (Price)", min_value=0.0, step=0.5, format="%.2f")
        
        submit_button = st.form_submit_button("🚀 إدارج الصنف في السجلات المعتمدة")
        
        if submit_button:
            if p_name == "":
                st.warning("الرجاء كتابة اسم الصنف أولاً.")
            else:
                try:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    
                    sql = "INSERT INTO Product (ProductID, PName, Price) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (p_id, p_name, p_price))
                    conn.commit()
                    
                    st.success(f"🎉 تم بنجاح إدراج الصنف: ({p_name}) في مخازن يمنى!")
                    cursor.close()
                    conn.close()
                    st.rerun()
                except mysql.connector.Error as err:
                    st.error(f"فشلت العملية: {err.msg}")

                    # =================================================================
# 📊 القسم الثالث الجديد: لوحة الاستعلامات والتقارير الذكية (لصق في النهاية)
# =================================================================
st.write("---")
st.markdown("<h2 style='color: #00A884; text-align: center;'>📊 لوحة التقارير والاستعلامات الذكية</h2>", unsafe_allow_html=True)

# تصميم الأزرار الستة على شكل لوحة تحكم ذكية (Grid)
col_q1, col_q2, col_q3 = st.columns(3)
col_q4, col_q5, col_q6 = st.columns(3)

# دالة مساعدة لتشغيل أي استعلام SQL وعرض نتيجته في جدول فخم
def run_custom_query(query_string, success_msg):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()
        
        if rows:
            st.markdown(f"<p style='color: #25D366; font-weight: bold;'>✅ {success_msg}</p>", unsafe_allow_html=True)
            res_df = pd.DataFrame(rows, columns=columns)
            st.dataframe(res_df, use_container_width=True)
        else:
            st.warning("لا توجد بيانات تطابق هذا الاستعلام حالياً.")
    except Exception as err:
        st.error(f"خطأ أثناء تنفيذ الاستعلام: {err}")

# 1. زر المنتجات الرخيصة
with col_q1:
    if st.button("🪙 المنتجات الشعبية الاقتصاديّة (تحت 20 ج.م)"):
        st.session_state['active_query'] = 'q1'

# 2. زر ترتيب المنتجات من الأغلى للأرخص
with col_q2:
    if st.button("📈 ترتيب المخزن (من الأغلى للأرخص)"):
        st.session_state['active_query'] = 'q2'

# 3. زر البحث الذكي عن عائلة النسكافيه
with col_q3:
    if st.button("☕ عرض عائلة ومنتجات النسكافيه"):
        st.session_state['active_query'] = 'q3'

# 4. زر متوسط الأسعار
with col_q4:
    if st.button("📊 حساب متوسط أسعار السلع"):
        st.session_state['active_query'] = 'q4'

# 5. زر إجمالي القيمة الماليّة للمخزن
with col_q5:
    if st.button("💰 حساب القيمة المالية الإجمالية للماركت"):
        st.session_state['active_query'] = 'q5'

# 6. زر المنتجات المتوسطة
with col_q6:
    if st.button("🍉 عرض المنتجات المتوسطة (من 15 إلى 50 ج.م)"):
        st.session_state['active_query'] = 'q6'

# عرض نتائج الاستعلام المختار أسفل الأزرار مباشرة في صندوق مخصص
st.write("---")
if 'active_query' in st.session_state:
    current_q = st.session_state['active_query']
    
    if current_q == 'q1':
        st.markdown("<h5 style='color: #E9EDEF;'>🪙 قائمة المنتجات تحت 20 جنيه:</h5>", unsafe_allow_html=True)
        run_custom_query("SELECT * FROM Product WHERE Price < 20.00", "تم تصفية السلع الاقتصادية بنجاح!")
        
    elif current_q == 'q2':
        st.markdown("<h5 style='color: #E9EDEF;'>📈 ترتيب المنتجات تنازلياً حسب السعر:</h5>", unsafe_allow_html=True)
        run_custom_query("SELECT * FROM Product ORDER BY Price DESC", "تم ترتيب الرفوف من الأغلى للأرخص!")
        
    elif current_q == 'q3':
        st.markdown("<h5 style='color: #E9EDEF;'>☕ السلع التي تحتوي على اسم 'نسكافيه':</h5>", unsafe_allow_html=True)
        run_custom_query("SELECT * FROM Product WHERE PName LIKE '%نسكافيه%'", "تم العثور على عائلة النسكافيه المتاحة!")
        
    elif current_q == 'q4':
        st.markdown("<h5 style='color: #E9EDEF;'>📊 المتوسط الحسابي لأسعار المنتجات:</h5>", unsafe_allow_html=True)
        run_custom_query("SELECT AVG(Price) AS 'متوسط سعر البضاعة (ج.م)' FROM Product", "تم حساب متوسط الأسعار الحقيقي!")
        
    elif current_q == 'q5':
        st.markdown("<h5 style='color: #E9EDEF;'>💰 إجمالي القيمة المادية للبضاعة المتوفرة:</h5>", unsafe_allow_html=True)
        run_custom_query("SELECT SUM(Price) AS 'إجمالي رأس مال المخزن (ج.م)' FROM Product", "تم جرد وحساب إجمالي قيمة الماركت بالكامل!")
        
    elif current_q == 'q6':
        st.markdown("<h5 style='color: #E9EDEF;'>🍉 المنتجات التي تقع أسعارها بين 15 و 50 جنيه:</h5>", unsafe_allow_html=True)
        run_custom_query("SELECT * FROM Product WHERE Price BETWEEN 15.00 AND 50.00", "تم حصر السلع ذات الفئة السعرية المتوسطة!")