from tabs.tab import TabInterface
import streamlit as st


class PassosMagicosONUODSTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[ONU]", divider="blue")
            st.markdown(
                "A **:blue[Organização das Nações Unidas (ONU)]**, fundada em 24 de outubro de 1945, é uma entidade internacional que visa promover a paz, a segurança, a cooperação internacional e os direitos humanos, contando atualmente com 193 Estados-membros. A **:blue[ONU]** atua em diversas áreas, incluindo desenvolvimento econômico e social, saúde, educação, meio ambiente e assistência humanitária, através de seus principais órgãos como a Assembleia Geral, o Conselho de Segurança, o Secretariado, o Conselho Econômico e Social, e o Tribunal Internacional de Justiça, além de várias agências especializadas como a OMS, UNESCO e UNICEF."
            )

            st.subheader(":blue[ODS]", divider="blue")
            st.markdown(
                """
                    Os **:blue[Objetivos de Desenvolvimento Sustentável (ODS)]** da **:blue[ONU]** são **:orange[17 metas]** globais adotadas em 2015, como parte da Agenda 2030 para o Desenvolvimento Sustentável. Esses objetivos buscam acabar com a pobreza, proteger o meio ambiente e garantir que todas as pessoas tenham paz e prosperidade até 2030. São elas:
                    1. **:blue[Erradicação da Pobreza:]** Acabar com a pobreza em todas as suas formas e em todos os lugares.
                    2. **:blue[Fome Zero e Agricultura Sustentável:]** Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição, e promover a agricultura sustentável.
                    3. **:blue[Saúde e Bem-Estar:]** Garantir uma vida saudável e promover o bem-estar para todos em todas as idades.
                    4. **:blue[Educação de Qualidade:]** Garantir educação inclusiva e equitativa de qualidade e promover oportunidades de aprendizagem ao longo da vida para todos.
                    5. **:blue[Igualdade de Gênero:]** Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas.
                    6. **:blue[Água Potável e Saneamento:]** Garantir disponibilidade e manejo sustentável da água e saneamento para todos.
                    7. **:blue[Energia Limpa e Acessível:]** Garantir acesso a fontes de energia acessíveis, confiáveis, sustentáveis e modernas para todos.
                    8. **:blue[Trabalho Decente e Crescimento Econômico:]** Promover o crescimento econômico sustentado, inclusivo e sustentável, emprego pleno e produtivo e trabalho decente para todos.
                    9. **:blue[Indústria, Inovação e Infraestrutura:]** Construir infraestruturas resilientes, promover a industrialização inclusiva e sustentável e fomentar a inovação.
                    10. **:blue[Redução das Desigualdades:]** Reduzir a desigualdade dentro dos países e entre eles.
                    11. **:blue[Cidades e Comunidades Sustentáveis:]** Tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis.
                    12. **:blue[Consumo e Produção Responsáveis:]** Assegurar padrões de produção e de consumo sustentáveis.
                    13. **:blue[Ação contra a Mudança Global do Clima:]** Tomar medidas urgentes para combater a mudança climática e seus impactos.
                    14. **:blue[Vida na Água:]** Conservar e usar de forma sustentável os oceanos, mares e recursos marinhos para o desenvolvimento sustentável.
                    15. **:blue[Vida Terrestre:]** Proteger, recuperar e promover o uso sustentável dos ecossistemas terrestres, gerir de forma sustentável as florestas, combater a desertificação, deter e reverter a degradação da terra e deter a perda de biodiversidade.
                    16. **:blue[Paz, Justiça e Instituições Eficazes:]** Promover sociedades pacíficas e inclusivas para o desenvolvimento sustentável, proporcionar o acesso à justiça para todos e construir instituições eficazes, responsáveis e inclusivas em todos os níveis.
                    17. **:blue[Parcerias e Meios de Implementação:]** Fortalecer os meios de implementação e revitalizar a parceria global para o desenvolvimento sustentável.

                    Esses objetivos interconectados são projetados para serem alcançados em conjunto, reconhecendo que ações em uma área afetarão os resultados em outras e que o desenvolvimento deve equilibrar a sustentabilidade social, econômica e ambiental.<br/><br/>
                    **:orange[A ONG Passos Mágicos apoia os Objetivos de Desenvolvimento Sustentável da ONU, especialmente os ODS 1, 4, 5, 8 e 10]**. Eles trabalham para acabar com a pobreza, garantir educação de qualidade, promover a igualdade de gênero, preparar jovens para o mercado de trabalho e reduzir desigualdades. A ONG oferece recursos e oportunidades para comunidades vulneráveis, ajudando a criar uma sociedade mais justa e igualitária.
            """,
                unsafe_allow_html=True,
            )
