import streamlit as st

# Dicionário com os significados dos Odús
odus = {
    1: ("OKANRAN", "Odu regido por Exu. Você parece ser agressivo, mas na verdade está apenas lutando para preservar a independência da qual muito se orgulha. Você não poupa esforços para atingir seus objetivos, mas deve tomar cuidado para não arrumar inimigos à toa."),
    2: ("EJIOKÔ", "Odu regido pelos Ibejis e Ogun. Você se mostra calmo no comportamento e seguro nas decisões, mas na sua mente sempre existem dúvidas. Não tenha medo de externar estas incertezas. Como muitas pessoas o amam, você acabará recebendo bons conselhos."),
    3: ("ETA-OGUNDÁ", "Odu regido por Ogun e Obaluaiê. A obstinação que se traduz em agitação e inconformismo, é uma das suas principais características. Mas, se usar suas qualidades, como a coragem, criatividade e a perseverança, conseguirá o que mais anseia: o poder e o sucesso."),
    4: ("YROSUN", "Odu regido por Iansã, Iemanjá. Sempre sereno e disposto a ver tudo com muita clareza e objetividade, você sabe resolver situações confusas ou tumultuadas. Tem plena consciência da sua força moral e não hesita em usá-la para atingir todas as suas metas."),
    5: ("OXÉ", "Odu regido por Oxum e Logun Edê. Sensível e sempre atento, você é uma pessoa sempre disposta a proporcionar alegria aos outros. Mas há momentos nos quais você precisa de isolamento para poder refletir, pois preza muito sua liberdade e, sobretudo, seu, crescimento."),
    6: ("OBARÁ", "Odu regido por Oxossi e Xangô. Você luta com unhas e dentes pelo que quer e geralmente consegue muito sucesso material. Mas, no amor precisa entender que não pode exigir demais dos outros."),
    7: ("ODI", "Odu regido por Omolu e Exu. Você realmente está satisfeito com o que consegue. Mas não fica se lamentando. Prefere ir à luta. Caso aprenda com clareza seus objetivos, alcançará grandes êxitos."),
    8: ("EJIONILE", "Odu regido por Oxaguiãn, Ogun e Xango Airá. Sua agilidade mental faz de você uma pessoa falante e muito ativa. Além disso, você gosta de poder e prestígio, por isso luta com muita intensidade pra chegar ao topo. Muitas vezes tempestuoso, e incontrolavel, mas seu senso de justiça o impede de prejudicar quem quer que seja."),
    9: ("OSÁ", "Odu regido por Iemanjá e Iansã. Você é uma pessoa que gosta de estudar cuidadosamente todas as coisas a sua volta, tem uma larga visão do mundo, por isso esta sempre pronto a poder ajudar, seja quem for. Dica: Se quiser manter a paz no seu dia a dia sera preciso aprender a não deixar fatos externos interferir em sua vida pessoal."),
    10: ("OFUN", "Odu regido por Oxalá. Seu jeitão rabugento é apenas um escudo para que os outros não abusem da sua boa vontade e sensibilidade. No fundo, você é uma pessoa serena, que se adapta aos autos e baixos da vida."),
    11: ("OWANRIN", "Orixás Chave: Oyá, Exú Odara, Erinlé (Odé), Oshumaré, Iyami Osorongá \n Temas principais: Destruição, Verdade, Gratidão, Restauração, Resistência, Fé, Descanso, Paciência \n Características Primárias: Owonrin Meji está associado a mudanças repentinas, conflitos e imprevisibilidade. Significa um período de turbulência onde a adaptabilidade e o raciocínio rápido são cruciais. Interpretações comuns: Quando Owonrin Meji aparece, sugere que a consulta pode estar entrando em um momento de turbulência e conflito. Este Odu aconselha a prontidão para enfrentar os desafios de frente e a importância de permanecer flexível e de mente aberta diante da mudança."),
    12: ("EJILAXEBORÁ", "Odu regido por Xangô. Sua principal virtude é o amor à justiça, que algumas vezes se transforma em intolerância com os erros alheios. Nessas ocasiões, você deve se voltar para outras de suas qualidades: a dedicação, que lhe permite ajudar todas as pessoas."),
    13: ("EJI-OLOGBON", "Odu regido por Nanã e Obaluaiê. Você está quase sempre um pouco deprimido. Só faz o que quer quando quer o como quer. Mas, como tem grande capacidade de reflexão, acaba se adaptando e consegue viver bem com os outros."),
    14: ("IKÁ-MEJI", "Odu regido por Oxumarê. Paciência e sabedoria são suas principais características. Versátil, você se dá bem em qualquer atividade. Poderá passar por provações materiais e sentimentais, mas sempre saberá reencontrar o caminho para a felicidade."),
    15: ("OBE-OGUNDÁ", "Odu regido por Ogun, Iemanjá, Omolu e Obá. Você uma pessoa rebelde e cheia de vontades, que muitas vezes não resiste a defender seu ponto de vista mesmo depois que percebe que está errado. Por isso, deve tomar cuidado para não se deixar dominar pelo nervosismo."),
    16: ("ALAFIÁ", "Odu regido por Oxalá e Orumilá. Suas principais características são a tranqüilidade e alegria. Amante da paz, você cria um clima de harmonia á sua volta. Se mantiver o equilíbrio, sem dúvida alcançará o sucesso.")
}

def reduzir(numero):
    while numero > 16:
        numero = sum(int(d) for d in str(numero))
    return numero

def calcular_5_odus(data):
    digitos = [int(d) for d in data if d.isdigit()]
    if len(digitos) != 8:
        return None
    
    col1 = digitos[0] + digitos[2] + digitos[4] + digitos[6]
    col2 = digitos[1] + digitos[3] + digitos[5] + digitos[7]

    testa = reduzir(col2)
    nuca = reduzir(col1)
    fronte_direita = reduzir(testa + nuca)
    fronte_esquerda = reduzir(testa + nuca + fronte_direita)
    centro = reduzir(sum(digitos))

    return {
        "Cabeça": nuca,
        "Pés": testa,
        "Direita": fronte_direita,
        "Esquerda": fronte_esquerda,
        "Centro (Abi Odú)": centro
    }

st.set_page_config(page_title="Calculadora de Odús", page_icon="🔮")
st.title("🔮 Calculadora dos 5 Odús de Nascimento")

data = st.text_input("Digite sua data de nascimento (dd/mm/aaaa):")

if st.button("Calcular Odús"):
    resultado = calcular_5_odus(data)
    if resultado:
        st.subheader("✨ Seus Odús:")
        for ponto, numero in resultado.items():
            nome, significado = odus[numero]
            with st.expander(f"{ponto}: {numero} - {nome}"):
                st.markdown(f"**Significado:** {significado}")
    else:
        st.error("Data inválida. Use o formato dd/mm/aaaa.")






st.markdown("---")  # linha horizontal para separar

st.markdown(
    """
    <p style="text-align:center; font-size:12px; color:gray;">
    Desenvolvido por Igor Vinícius. <br>
    Baseado em conhecimentos tradicionais dos Odús. <br>
    
    
    """,
    unsafe_allow_html=True
)

