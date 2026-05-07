import streamlit as st
import qrcode
from PIL import Image
import io

# 页面基础设置
st.set_page_config(
    page_title="千物新语 · 文物朋友圈",
    page_icon="🏺",
    layout="wide"
)

# 标题与项目说明
st.title("🏺 千物新语 · 文物朋友圈")
st.subheader("让国宝，拥有自己的社交动态")
st.markdown("---")

# ✅ 所有图片 100% 英文名称，无中文
relics = [
    {
        "name": "孝端皇后九龙九凤冠",
        "era": "明代万历年间",
        "intro": "明神宗孝端皇后的礼冠，定陵出土国宝。以黄金为骨，点翠凤凰栩栩如生，镶嵌上百颗红蓝宝石与珍珠，是明代宫廷首饰的巅峰之作。",
        "text": "大明皇后的限定款，戴上我，你就是后宫里最耀眼的存在。历经四百年，依旧珠光宝气，自带王者气场✨",
        "img": "fengguan.jpg"
    },
    {
        "name": "后母戊鼎（司母戊鼎）",
        "era": "商代晚期",
        "intro": "现存最大最重的青铜礼器，重832.84公斤，是商代青铜铸造的巅峰。器身纹饰威严庄重，见证了商代王室祭祀礼仪，被誉为“镇国之宝”。",
        "text": "我是殷商的镇国重器，沉默三千年，依旧是青铜界的‘天花板’。见过王朝更迭，也见过人间烟火，我的纹路里，藏着整个商朝的故事。",
        "img": "ding.jpg"
    },
    {
        "name": "四羊方尊",
        "era": "商代晚期",
        "intro": "现存商代青铜方尊中最大的一件，以“四羊”造型闻名。将线雕、浮雕、圆雕完美融合，造型雄奇，纹饰精美，被誉为“臻于极致的青铜典范”。",
        "text": "我是商代最靓的‘四羊’组合，头顶着盛世的光芒，脚踏着千年的时光。我的纹路里，藏着商代工匠的浪漫与智慧。",
        "img": "yang.jpg"
    },
    {
        "name": "越王勾践剑",
        "era": "春秋时期",
        "intro": "越王勾践的佩剑，历经两千余年不锈，剑身寒光逼人，菱形暗纹精美绝伦，被誉为“天下第一剑”，是吴越青铜剑的巅峰之作。",
        "text": "我是越王勾践的佩剑，见证了卧薪尝胆的隐忍，也见证了破吴归越的荣光。千年不锈，锋芒依旧，这就是王者的底气。",
        "img": "jian.jpg"
    },
    {
        "name": "西周青铜提梁卣",
        "era": "西周早期",
        "intro": "西周盛酒礼器，造型复杂华丽，提梁龙纹、器身兽面纹栩栩如生，是西周青铜工艺的杰出代表，也是贵族等级与权力的象征。",
        "text": "我是西周贵族的‘限定酒壶’，提梁上的神兽守护着千年佳酿，器身上的纹路诉说着礼乐文明的故事。",
        "img": "you.jpg"
    }
]

# 循环展示朋友圈
for idx, relic in enumerate(relics):
    with st.container():
        st.markdown(f"### 🏺 {relic['name']}")
        st.caption(f"年代：{relic['era']}")
        st.info(relic['intro'])
        st.write(relic['text'])

        # ✅ 图片只使用英文名称，绝对不出现中文
        st.image(relic["img"], width=700)

        # 点赞
        if st.button(f"❤️ 点赞", key=f"like_{idx}"):
            st.success("点赞成功！")

        # 评论
        comment = st.text_input("发表评论", key=f"comment_{idx}")
        if st.button("提交评论", key=f"submit_{idx}"):
            if comment:
                st.info(f"你的评论：{comment}")

        st.markdown("---")

# AI 生成文案
st.markdown("## 🤖 AI 智能生成文物朋友圈文案")
relic_name = st.text_input("输入文物名称")
if st.button("生成文案") and relic_name:
    ai_text = f"我是【{relic_name}】，沉睡千年，见证华夏岁月悠悠，历史长河漫漫。"
    st.success(ai_text)

# 二维码
st.markdown("## 📱 扫码访问项目")
qr = qrcode.make("http://10.0.26.242:8501")
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)
st.image(Image.open(buf), width=250)

# 项目介绍
st.markdown("## 🎨 项目说明")
st.write("《千物新语》是智能文化创意作品，以文物朋友圈为核心，包含点赞、评论、AI生成、二维码等功能。")