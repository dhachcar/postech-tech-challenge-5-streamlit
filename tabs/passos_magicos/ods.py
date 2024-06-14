from tabs.tab import TabInterface
import streamlit as st


class PassosMagicosODS(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                "A Organização das Nações Unidas (ONU), fundada em 24 de outubro de 1945, é uma entidade internacional que visa promover a paz, a segurança, a cooperação internacional e os direitos humanos, contando atualmente com 193 Estados-membros. A ONU atua em diversas áreas, incluindo desenvolvimento econômico e social, saúde, educação, meio ambiente e assistência humanitária, através de seus principais órgãos como a Assembleia Geral, o Conselho de Segurança, o Secretariado, o Conselho Econômico e Social, e o Tribunal Internacional de Justiça, além de várias agências especializadas como a OMS, UNESCO e UNICEF."
            )

            st.markdown(
                """
                    Os Objetivos de Desenvolvimento Sustentável (ODS) da ONU são um conjunto de 17 metas globais adotadas pela Assembleia Geral das Nações Unidas em 2015, como parte da Agenda 2030 para o Desenvolvimento Sustentável. Esses objetivos visam erradicar a pobreza, proteger o planeta e garantir que todas as pessoas desfrutem de paz e prosperidade até 2030. Os ODS sucedem os Objetivos de Desenvolvimento do Milênio (ODM) e são mais abrangentes, abordando uma ampla gama de questões interconectadas.

                    Os 17 ODS são:

                    1) Erradicação da Pobreza: Acabar com a pobreza em todas as suas formas e em todos os lugares.
                    2) Fome Zero e Agricultura Sustentável: Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição, e promover a agricultura sustentável.
                    3) Saúde e Bem-Estar: Garantir uma vida saudável e promover o bem-estar para todos em todas as idades.
                    4) Educação de Qualidade: Garantir educação inclusiva e equitativa de qualidade e promover oportunidades de aprendizagem ao longo da vida para todos.
                    5) Igualdade de Gênero: Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas.
                    6) Água Potável e Saneamento: Garantir disponibilidade e manejo sustentável da água e saneamento para todos.
                    7) Energia Limpa e Acessível: Garantir acesso a fontes de energia acessíveis, confiáveis, sustentáveis e modernas para todos.
                    8) Trabalho Decente e Crescimento Econômico: Promover o crescimento econômico sustentado, inclusivo e sustentável, emprego pleno e produtivo e trabalho decente para todos.
                    9) Indústria, Inovação e Infraestrutura: Construir infraestruturas resilientes, promover a industrialização inclusiva e sustentável e fomentar a inovação.
                    10) Redução das Desigualdades: Reduzir a desigualdade dentro dos países e entre eles.
                    11) Cidades e Comunidades Sustentáveis: Tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis.
                    12) Consumo e Produção Responsáveis: Assegurar padrões de produção e de consumo sustentáveis.
                    13) Ação contra a Mudança Global do Clima: Tomar medidas urgentes para combater a mudança climática e seus impactos.
                    14) Vida na Água: Conservar e usar de forma sustentável os oceanos, mares e recursos marinhos para o desenvolvimento sustentável.
                    15) Vida Terrestre: Proteger, recuperar e promover o uso sustentável dos ecossistemas terrestres, gerir de forma sustentável as florestas, combater a desertificação, deter e reverter a degradação da terra e deter a perda de biodiversidade.
                    16) Paz, Justiça e Instituições Eficazes: Promover sociedades pacíficas e inclusivas para o desenvolvimento sustentável, proporcionar o acesso à justiça para todos e construir instituições eficazes, responsáveis e inclusivas em todos os níveis.
                    17) Parcerias e Meios de Implementação: Fortalecer os meios de implementação e revitalizar a parceria global para o desenvolvimento sustentável.
                    Esses objetivos interconectados são projetados para serem alcançados em conjunto, reconhecendo que ações em uma área afetarão os resultados em outras e que o desenvolvimento deve equilibrar a sustentabilidade social, econômica e ambiental."""
            )

            st.markdown(
                """ 
                ODS almejados pela ONG Passos Mágicos:
                - ODS 1 Erradicação da Pobreza
                - ODS 4 Educação
                - ODS 5 Igualdade de gênero
                - ODS 8 Trabalhos descente
                - ODS 10 Redução das desigualdades
                """
            )
