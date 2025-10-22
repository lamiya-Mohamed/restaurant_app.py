import streamlit as st

# عنوان التطبيق
st.title("🍽️ مطعم البرمجة السعيدة")

st.write("مرحبًا بك في تطبيق طلبات المطعم! اختر وجبتك واحسب الفاتورة النهائية 👇")

# قائمة الوجبات
menu = {
    "برجر لحم": 80,
    "بيتزا مارجريتا": 100,
    "فاهيتا دجاج": 120,
    "بطاطس مقلية": 30,
    "بيبسي": 20,
    "مياه معدنية": 10
}

# عرض الخيارات
st.subheader("اختر الوجبات:")
order = {}
for item, price in menu.items():
    quantity = st.number_input(f"{item} - {price} جنيه", min_value=0, max_value=10, key=item)
    if quantity > 0:
        order[item] = quantity

# حساب المجموع
if order:
    st.subheader("💰 الفاتورة:")
    total = sum(menu[item] * qty for item, qty in order.items())
    for item, qty in order.items():
        st.write(f"- {item} × {qty} = {menu[item] * qty} جنيه")
    st.write(f"### الإجمالي: {total} جنيه")

    # إضافة خصم بسيط
    discount = 0
    if total > 300:
        discount = total * 0.1
        st.success(f"🎉 حصلت على خصم 10% = {discount} جنيه")
        total -= discount

    st.write(f"## 💵 المبلغ النهائي: {total} جنيه")

else:
    st.info("لم تختر أي وجبة بعد 🍔")

# تذييل
st.markdown("---")
st.caption("تطبيق تجريبي بسيط باستخدام Streamlit ❤️")
