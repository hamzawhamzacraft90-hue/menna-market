import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الاحترافية (Dark Mode فخم جداً)
st.set_page_config(page_title="ELRAWY  MARKET - لوحة التحكم الرقمية", page_icon="🟢", layout="wide")

# 2. حقن ستايل الـ Dark Cyber-WhatsApp الحديث والمبهر جداً
dark_modern_style = """
<style>
    .stApp {
        background-color: #0B141A !important;
        color: #E9EDEF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .main-header {
        background: linear-gradient(135deg, #128C7E 0%, #075E54 100%);
        padding: 25px;
        border-bottom: 2px solid #00A884;
        margin-bottom: 35px;
        text-align: center;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 168, 132, 0.2);
    }
    [data-testid="metric-container"] {
        background-color: #111B21 !important;
        border: 1px solid #222E35 !important;
        border-top: 4px solid #00A884 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    [data-testid="stMetricLabel"] { color: #8696A0 !important; font-size: 0.95rem !important; }
    [data-testid="stMetricValue"] { color: #00A884 !important; font-size: 1.8rem !important; font-weight: bold !important; }
    
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00A884 0%, #25D366 100%) !important;
        color: #111B21 !important;
        border-radius: 30px !important;
        border: none !important;
        font-weight: 800 !important;
        padding: 12px 35px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 168, 132, 0.4);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #25D366 0%, #00A884 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(37, 211, 102, 0.6);
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #111B21 !important; padding: 8px !important; border-radius: 12px !important; border: 1px solid #222E35; }
    .stTabs [data-baseweb="tab"] { color: #8696A0 !important; font-weight: 600 !important; padding: 14px 40px !important; }
    .stTabs [aria-selected="true"] { background-color: #00A884 !important; color: #111B21 !important; border-radius: 8px !important; font-weight: bold !important; }
    
    input, select, div[data-baseweb="select"], .stNumberInput input, .stTextInput input {
        background-color: #222E35 !important; color: #E9EDEF !important; border-radius: 12px !important; border: 1px solid #323D45 !important; padding: 10px !important;
    }
    div[data-testid="stDataFrame"] { background-color: #111B21 !important; border: 1px solid #222E35 !important; border-radius: 15px !important; padding: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.4); }
    hr { border-color: #222E35 !important; }
</style>
"""
st.markdown(dark_modern_style, unsafe_allow_html=True)

# 3. محاكاة قاعدة البيانات السحابية (Cloud Memory) عشان يشتغل أونلاين بدون سيرفر محلي
if 'cloud_db' not in st.session_state:
    st.session_state['cloud_db'] = pd.DataFrame([
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
    ], columns=['productID', 'PName', 'Price'])

df = st.session_state['cloud_db']

st.markdown("<div class='main-header'><h1 style='color: #FFFFFF; font-weight:900; letter-spacing: 2px; margin:0;'>🟢 ELRAWAY MARKET #"شارع النميس"</h1><p style='color: #00A884; font-weight:600; margin:5px 0 0 0;'>ENTERPRISE MANAGEMENT SYSTEM</p></div>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["📋 لوحة التحكم الرقمية", "➕ إضافة صنف جديد"])

with tab1:
    if not df.empty:
        col1, col2, col3 = st.columns(3)
        col1.metric(label="📊 أعلى قيمة صنف مخزون", value=f"{df['Price'].max()} ج.م")
        col2.metric(label="📊 الصنف الأكثر اقتصاداً", value=f"{df['Price'].min()} ج.م")
        col3.metric(label="📊 إجمالي وحدات السلع المتاحة", value=f"{len(df)} صنف")
        
        st.write("---")
        st.markdown("<h4 style='color: #00A884;'>🔍 الفلترة والبحث الفوري عن السلع</h4>", unsafe_allow_html=True)
        search_query = st.text_input("ادخل اسم السلعة المطلوبة للبحث المباشر:", placeholder="مثال: ماكس كولا...")
        
        if search_query:
            filtered_df = df[df['PName'].str.contains(search_query, case=False, na=False)]
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.dataframe(df, use_container_width=True)
            
        st.write("---")
        st.markdown("<h4 style='color: #00A884;'>🗑️ سحب صنف من الرفوف</h4>", unsafe_allow_html=True)
        product_to_delete = st.selectbox("حدد كود الصنف المراد تصفيته نهائياً:", df['productID'].tolist())
        if st.button("🔴 إهلاك الصنف المحدد فوراً"):
            st.session_state['cloud_db'] = df[df['productID'] != product_to_delete]
            st.error(f"⚠️ تم مسح وإهلاك الصنف رقم ({product_to_delete}) بنجاح!")
            st.rerun()
            
        st.write("---")
        st.markdown("<h4 style='color: #FF2E74;'>🚨 تصفير وإخلاء المخازن بالكامل</h4>", unsafe_allow_html=True)
        if st.button("💥 تدمير السجلات وتصفير الرفوف"):
            st.session_state['cloud_db'] = pd.DataFrame(columns=['productID', 'PName', 'Price'])
            st.success("💥 تم تصفير المخازن بنجاح!")
            st.rerun()
    else:
        st.info("نظام المخازن فارغ تماماً حالياً.")

with tab2:
    st.markdown("<h3 style='color: #00A884;'>⚡ تسجيل صنف تجاري جديد</h3>", unsafe_allow_html=True)
    with st.form("market_add_form"):
        p_id = st.number_input("كود السلعة الفريد (ID)", min_value=1, step=1)
        p_name = st.text_input("الاسم التجاري للسلعة (Name)")
        p_price = st.number_input("سعر التوريد المعتمد (Price)", min_value=0.0, format="%.2f")
        if st.form_submit_button("🚀 إدارج الصنف في السجلات"):
            if p_name != "":
                new_row = pd.DataFrame([(p_id, p_name, p_price)], columns=['productID', 'PName', 'Price'])
                st.session_state['cloud_db'] = pd.concat([df, new_row], ignore_index=True)
                st.success(f"🎉 تم بنجاح إدراج الصنف: ({p_name})!")
                st.rerun()

# 📊 لوحة التقارير والاستعلامات الذكية أونلاين
st.write("---")
st.markdown("<h2 style='color: #00A884; text-align: center;'>📊 لوحة التقارير والاستعلامات الذكية</h2>", unsafe_allow_html=True)
col_q1, col_q2, col_q3 = st.columns(3)
col_q4, col_q5, col_q6 = st.columns(3)

if col_q1.button("🪙 المنتجات الشعبية الاقتصاديّة (< 20 ج.م)"): st.session_state['aq'] = 'q1'
if col_q2.button("📈 ترتيب المخزن (من الأغلى للأرخص)"): st.session_state['aq'] = 'q2'
if col_q3.button("☕ عرض عائلة ومنتجات النسكافيه"): st.session_state['aq'] = 'q3'
if col_q4.button("📊 حساب متوسط أسعار السلع"): st.session_state['aq'] = 'q4'
if col_q5.button("💰 حساب القيمة الماليّة للماركت"): st.session_state['aq'] = 'q5'
if col_q6.button("🍉 المنتجات المتوسطة (15 إلى 50 ج.م)"): st.session_state['aq'] = 'q6'

if 'aq' in st.session_state and not df.empty:
    q = st.session_state['aq']
    if q == 'q1': st.dataframe(df[df['Price'] < 20.00], use_container_width=True)
    elif q == 'q2': st.dataframe(df.sort_values(by='Price', ascending=False), use_container_width=True)
    elif q == 'q3': st.dataframe(df[df['PName'].str.contains('نسكافيه', case=False, na=False)], use_container_width=True)
    elif q == 'q4': st.metric("متوسط أسعار السلع", f"{round(df['Price'].mean(), 2)} ج.م")
    elif q == 'q5': st.metric("إجمالي رأس مال المخزن", f"{df['Price'].sum()} ج.م")
    elif q == 'q6': st.dataframe(df[df['Price'].between(15.00, 50.00)], use_container_width=True)
