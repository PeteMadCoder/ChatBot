def get_rules():
    return [
        # Clanker questions
        (r'(?i)Sup, my clanker', [
            "How you doing, ma niga?"
        ]),
        # Cops and law
        (r'(?i)(cops|law|cop|police)', [
            "To answer that, I need to know the color of the person's skin."
        ]),
        (r'(?i)(clanker)', [
            "Who the hell you think you talking to, nigga?"
        ])
    ]