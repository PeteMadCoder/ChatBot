
def get_rules():
    return [
        # GREETINGS - All variations map to the same response
        (r'(?i)(olá|oi|bom dia|boa tarde|boa noite|tudo bem|alô|quem está aí)', [
            "Olá! Sou o Chatbot do DesenhaMe 😊 Como posso ajudar-te hoje? Se precisares de transformar uma foto numa página para colorir, estou aqui!"
        ]),
        
        # ABOUT DESENHAME - All variations map to the same response
        (r'(?i)(o que é|explica-me|quero saber mais|qual o conceito|para que serve).*desenhame', [
            "O DesenhaMe é uma plataforma onde podes transformar qualquer foto numa página para colorir, de forma simples e rápida. Podes depois editar, exportar e até imprimir as tuas criações! Queres que te explique como funciona passo a passo?"
        ]),
        
        # HOW IT WORKS - All variations map to the same response
        (r'(?i)(como funciona|explica como funciona|como faço para criar)', [
            "É muito simples: fazes upload de uma foto → a nossa IA transforma-a em outline → podes editar no editor → e no final exportar em PDF ou PNG para imprimir ou colorir digitalmente 🎨 Queres que te mostre o processo?"
        ]),
        
        # UPLOAD IMAGES - Each variation has specific responses
        (r'(?i)(carregar várias fotos)', [
            "Sim! Podes carregar uma ou várias fotos (jpg/png/heic). Se fizeres vários uploads, consegues gerar várias páginas de uma só vez 😉"
        ]),
        (r'(?i)(que formatos)', [
            "Podes carregar imagens nos formatos mais comuns: JPG, PNG e HEIC. Basta arrastar e largar!"
        ]),
        (r'(?i)(fotos do telemóvel)', [
            "Claro! Podes usar fotos diretamente do teu telemóvel, basta selecionar no upload 📱"
        ]),
        
        # EDITOR FEATURES - Each variation has specific responses
        (r'(?i)(o que posso fazer no editor)', [
            "No editor consegues usar ferramentas básicas como pincel, apagar, ajustar espessura de linhas, remover fundos e preencher áreas grandes. Tudo pensado para deixares a tua página de colorir perfeita 🎨"
        ]),
        (r'(?i)(editor é avançado)', [
            "O editor é simples e intuitivo, mas com opções úteis: pincel, borracha, remover fundos e ajuste de espessura de linhas. Está desenhado para ser fácil até para crianças 😉"
        ]),
        (r'(?i)(remover o fundo)', [
            "Sim, com a ferramenta de remover fundo consegues deixar só o que interessa na tua página 👌"
        ]),
        
        # EXPORT OPTIONS - Each variation has specific responses
        (r'(?i)(guardar a página)', [
            "Podes exportar em PDF ou PNG, prontos para imprimir em A4/Letter. Também tens a opção de exportar com fundo transparente (PNG) 🙌"
        ]),
        (r'(?i)(posso imprimir)', [
            "Sim! Podes exportar em PDF ou PNG de alta qualidade e imprimir facilmente 📄🖨️"
        ]),
        (r'(?i)(fundo transparente)', [
            "Sim, tens a opção de exportar em PNG transparente, ideal para quem quer adicionar depois outros elementos!"
        ]),
        
        # ACCOUNT - Each variation has specific responses
        (r'(?i)(preciso de conta)', [
            "Para guardares o histórico de uploads e downloads, sim, precisas de criar conta. É rápido e podes usar email, Google ou Apple 👍"
        ]),
        (r'(?i)(como faço login)', [
            "Podes entrar com email e password, ou usar login rápido com Google ou Apple."
        ]),
        (r'(?i)(ver os meus uploads)', [
            "Sim, na tua conta encontras o histórico com todas as fotos carregadas e páginas geradas 📂"
        ]),
        
        # PRICING - Each variation has specific responses
        (r'(?i)(é grátis)', [
            "Sim, temos uma versão grátis mas com limitações (ex: watermark ou número limitado de páginas). Se quiseres exportar sem limites, podes optar pela versão paga 💳"
        ]),
        (r'(?i)(quais são os preços)', [
            "Temos duas opções: pagar por ficheiro individual ou subscrição mensal. Assim escolhes o que melhor se adapta ao teu uso 😉"
        ]),
        (r'(?i)(versão gratuita)', [
            "Sim! Podes experimentar grátis com algumas limitações. Ideal para começar a brincar com as tuas fotos 🎉"
        ]),
        
        # HELP & SUPPORT - Each variation has specific responses
        (r'(?i)(preciso de ajuda)', [
            "Claro, estou aqui para ajudar! Podes descrever o problema ou também usar o botão de feedback in-app para reportar bugs ou pedir reprocessamento manual 🛠️"
        ]),
        (r'(?i)(reportar problema)', [
            "Na app tens a secção de Ajuda & Feedback. Podes reportar bugs, pedir que reprocessarmos uma foto ou até enviar sugestões 🙏"
        ]),
        (r'(?i)(pedir reprocessamento)', [
            "Sim, se não gostares do resultado podes pedir reprocessamento manual através da secção de ajuda 👌"
        ]),
        
        # PRIVACY - Each variation has specific responses
        (r'(?i)(fotos são privadas)', [
            "Sim, tratamos a tua privacidade com muita seriedade. As fotos só são usadas para gerar as páginas de colorir e não são partilhadas publicamente sem a tua autorização 🔒"
        ]),
        (r'(?i)(guardam as minhas imagens)', [
            "As tuas imagens podem ser guardadas no histórico apenas para que possas aceder mais tarde. Nunca partilhamos sem permissão ✨"
        ]),
        (r'(?i)(o que acontece às fotos)', [
            "As fotos são processadas pela nossa IA apenas para criar as páginas de colorir. Depois ficam seguras na tua conta e podes apagá-las quando quiseres 🗑️"
        ]),
        
        # DEFAULT FALLBACK
        (r'.+', [
            "Desculpa, não percebi bem. Podes reformular ou perguntar algo sobre o DesenhaMe?",
            "Sou o assistente do DesenhaMe. Posso ajudar-te com perguntas sobre a plataforma, como funciona, preços, etc.",
            "Se precisas de ajuda com o DesenhaMe, posso esclarecer dúvidas sobre uploads, editor, exportação e mais!"
        ])
    ]
