import streamlit as st
import json


def load_data():
    data = {
        {
            "american": {
                "title": "Kuchnia Amerykańska",
                "description": "Kuchnia amerykańska to bogactwo smaków i kulinarnych tradycji, które zyskały uznanie na całym świecie. To nie tylko fast foody i hamburgery, lecz także wyśmienite dania, które czerpią inspirację z wielu kultur. W Ameryce można znaleźć potrawy reprezentujące praktycznie każdy region świata, co sprawia, że kuchnia amerykańska jest niezwykle różnorodna i interesująca.",
                "img": {
                    "path": "assets/images/american/chocolate-banana-muffins.jpg",
                    "caption": "Bananowe Muffiny z Czekoladą"},
                "info": "Kuchnia amerykańska to zbiór różnorodnych smaków i tradycji kulinarnej, które odzwierciedlają różnorodność kulturową kraju. Choć często kojarzona z fast foodami i potrawami typu 'comfort food', takimi jak hamburgery, frytki czy hot dogi, to jednak amerykańska kuchnia oferuje znacznie więcej. Wpływy kulinarnych tradycji z całego świata sprawiają, że amerykańska kuchnia jest niezwykle zróżnicowana. Na przykład kuchnia południowa, znana jako southern cuisine, wyróżnia się wykorzystaniem marynat, duszenia i głębokiego smażenia, co daje intensywne smaki. Potrawy takie jak fried chicken, gumbo czy jambalaya są popularne w tej części Stanów Zjednoczonych. Z kolei kuchnia zachodnia, a zwłaszcza kalifornijska, jest znana z lekkości i zdrowego podejścia do jedzenia. Duży nacisk kładzie się tu na świeże składniki, warzywa, owoce morza i dania z grilla. Niezależnie od regionu, amerykańska kuchnia jest także obfituje w słodkie przysmaki, takie jak serniki, brownies czy ciasta, które są nieodłączną częścią amerykańskiego doświadczenia kulinarne."
            },
            "arabic": {
                "title": "Kuchnia Arabska",
                "description": "Kuchnia arabska to harmonia smaków i aromatów Bliskiego Wschodu. Obfituje w warzywa, przyprawy i aromatyczną oliwę z oliwek. Hummus, falafel czy kebaby to tylko niektóre z wyjątkowych dań, które zachwycają smakoszy na całym świecie.",
                "img": {
                    "path": "assets/images/arabic/falafel.jpg",
                    "caption": "Falafel in Sezamem"},
                "info": "Kuchnia arabska to niezwykle bogata i zróżnicowana kuchnia, która rozwijała się przez wieki w krajach Bliskiego Wschodu, Afryki Północnej i innych regionach arabskich. Jest to jedna z najstarszych i najbardziej wpływowych kuchni na świecie, znana ze swojej aromatycznej mieszanki przypraw, świeżych składników i wyjątkowych smaków. Arabska kuchnia opiera się głównie na oliwie z oliwek, świeżych ziołach i przyprawach, takich jak kumin, korzeń kolendry, gałka muszkatołowa i szafran. Warzywa, takie jak bakłażany, pomidory, cukinia i papryka, są powszechnie stosowane, często duszone w oliwie z oliwek z dodatkiem czosnku i ziół. Mięso, zwłaszcza jagnięcina, jest również ważnym składnikiem arabskich dań. Kebaby, kofty (mięsne kuleczki) i tagine (dania duszone w glinianym naczyniu) są popularne w całym regionie. Ryby i owoce morza są również powszechnie spożywane, zwłaszcza w krajach leżących nad Morzem Śródziemnym. Desery w kuchni arabskiej są słodkie i aromatyczne, często przygotowywane z baklawą (warstwowym ciastem z orzechami i miodem), halwą (słodką pastą z nasion sezamu) i rahat lukum (tureckie rarytasy z galaretki owocowej). Arabska kuchnia to nie tylko smak, ale także sposób życia, który celebruje gościnność, wspólną strawę i tradycje kulinarne przekazywane z pokolenia na pokolenie."
            },
            "french": {
                "title": "Kuchnia Francuska",
                "description": "Kuchnia francuska to kwintesencja elegancji i wyrafinowania kulinarnej sztuki. Znana z doskonałego połączenia smaków, świeżych składników i precyzyjnych technik gotowania, francuska kuchnia jest uważana za jedną z najbardziej wpływowych na świecie. Charakterystyczne dania obejmują escargots, foie gras, ratatouille, oraz tournée ziemniaki.",
                "img": {
                    "path": "assets/images/french/croissant.jpg",
                    "caption": "Klasyczne Croissanty"},
                "info": "Kuchnia francuska to niezwykła mieszanka smaków, aromatów i technik gotowania, która od wieków zachwyca koneserów na całym świecie. Charakteryzuje się bogactwem wykwintnych potraw, precyzyjnymi przygotowaniami i wykorzystaniem wysokiej jakości składników. Francuskie dania są znane z elegancji i perfekcji, której nie znajdziemy w żadnej innej kuchni. Wśród najbardziej znanych potraw znajduje się escargots (ślimaki), foie gras (pasztet z gęsich wątróbek), ratatouille (duszona mieszanka warzyw), czy quiche lorraine (tarta z boczkiem i serem). Francuscy kucharze słyną z mistrzowskiego wykorzystania maślanych sosów, jak beurre blanc czy hollandaise, oraz umiejętności przyrządzania delikatnych mięs, takich jak kurczak czy kaczka. W kuchni francuskiej ważne są także desery, takie jak crème brûlée, tarte tatin czy macarons, które stanowią doskonałe zakończenie wykwintnego posiłku. Kuchnia francuska to prawdziwa uczta dla zmysłów, która odzwierciedla bogactwo kultury i tradycji tego fascynującego kraju."
            },
            "polish": {
                "title": "Kuchnia Polska",
                "description": "Kuchnia polska to harmonia tradycji i smaków. Obfituje w aromatyczne zupy, jak barszcz czy żurek, oraz tradycyjne dania mięsne, takie jak pierogi czy bigos. Charakteryzuje się także wykorzystaniem świeżych składników, takich jak ziemniaki, kapusta i wieprzowina. To kuchnia, która serwuje niezapomniane smaki z dalekiej przeszłości, zachowując jednocześnie swoją autentyczność i oryginalność.",
                "img": {
                    "path": "assets/images/polish/easter-lamb.jpg",
                    "caption": "Baranek Wielkanocny"},
                "info": "Kuchnia polska jest niezwykle zróżnicowana i bogata w smaki, co sprawia, że jest jedną z najbardziej fascynujących kuchni świata. Charakteryzuje się ona wykorzystaniem świeżych, lokalnych składników oraz tradycyjnych receptur, przekazywanych z pokolenia na pokolenie. Jednym z najbardziej charakterystycznych elementów polskiej kuchni są zupy. Zupy takie jak barszcz, żurek czy krupnik są nieodłączną częścią tradycyjnych polskich obiadów. Wykorzystują one różnorodne składniki, takie jak kapusta, ziemniaki, grzyby czy mięso, co nadaje im niepowtarzalny smak i aromat. Kolejnym ważnym elementem polskiej kuchni są dania mięsne. Pierogi, gołąbki, bigos czy schabowy to tylko niektóre z popularnych dań mięsnych, które stanowią integralną część kuchni polskiej. Mięso często jest duszone, pieczone lub smażone, co nadaje mu charakterystyczny smak i aromat. Nie można zapomnieć o słodkościach. Kuchnia polska słynie z pysznych deserów, takich jak sernik, makowiec, szarlotka czy pączki. Te ciasta i słodkości są nieodłączną częścią tradycyjnych polskich świąt i uroczystości. Kuchnia polska to nie tylko smakowite potrawy, ale także bogata historia i tradycja, które przekazując się z pokolenia na pokolenie, nadają jej niepowtarzalny charakter."
            },
            "ukranian": {
                "title": "Kuchnia Ukraińska",
                "description": "Kuchnia ukraińska to bogactwo smaków i tradycji. Charakteryzuje się obfitością warzyw, ziół i świeżych składników, które tworzą wyjątkowe połączenia smakowe. Pierogi, barszcz ukraiński, czy sałatka 'wiosenna' to tylko niektóre z popularnych dań. Kuchnia ta ceniona jest za swoją autentyczność i prostotę, jednocześnie oferując wyjątkowe doznania kulinarno-kulturowe.",
                "img": {
                    "path": "assets/images/ukranian/borscht.jpg",
                    "caption": "Borscht"},
                "info": "Kuchnia ukraińska słynie z bogactwa smaków, tradycji i świeżych składników. Jest to kuchnia, która odzwierciedla historię i kulturę Ukrainy. Charakteryzuje się dużym wykorzystaniem warzyw, ziół i mięsa, zwłaszcza wieprzowiny, drób i ryb. Popularne dania ukraińskie to m.in. pierogi, barszcz ukraiński, sałatka 'wiosenna', czy też tradycyjne placki ziemniaczane zwane deruny. Kuchnia ukraińska jest również znana z wykorzystania produktów zbożowych, takich jak kasza gryczana czy płatki owsiane. Jednym z najbardziej znanych elementów kuchni ukraińskiej jest też wykorzystanie kiszonek, takich jak kiszona kapusta czy ogórki. Kuchnia ukraińska to także bogactwo smaków i aromatów, które czynią ją niezwykle atrakcyjną dla miłośników dobrego jedzenia."
            }
    }
    return data

def app():
    st.set_page_config(
        page_title="Smaki Globu")
    st.header(body="Smaki Globu", help="Odkryj smaki świata w jednym miejscu!", divider="gray")
    st.markdown("""
        <style>
            button p{
                font-weight: 700 !important;
            }
        </style>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        st.caption("""
                <p style='font-weight: 600'>
                   Smaki Globu są jak magiczne bramy, które przenoszą nas w podróż po kulturach i tradycjach.
                   Odkryj z nami bogactwo kulinarnych doświadczeń, które skrywają się w każdym kęsie!
                </p>
            """, unsafe_allow_html=True)

    with st.container(border=True):
        for c, j in enumerate(load_data().values(), 0):
            with st.container(border=True):
                st.title(j.get("title"))
                tab1, tab2 = st.tabs(["Wstęp", "Więcej"])
                with tab1:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"<p style='font-weight: 600'>{j.get('description')}</p>", unsafe_allow_html=True)
                    with col2:
                        img = j.get("img")
                        st.image(image=img["path"], caption=img["caption"].upper())
                with tab2:
                    st.write(j.get("info"))
                            
                        
                        
                # if st.button("Czytaj Więcej", type="secondary", key=c, use_container_width=True):
                #     st.switch_page("pages/american_cuisine.py")

if __name__ == "__main__":
    app()
