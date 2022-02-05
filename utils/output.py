from .exchanger import get_amount

text = {'DOLLAR to RUB': ["$", "₽"],
        'DOLLAR to EURO': ["$", "€"],
        'DOLLAR to BTC': ["$", "₿ (bitcoin)"],
        'DOLLAR to ETH': ["$", "Ξ (ethereum)" ]}


def output_text(currency: str, amount: float) -> str:
        cur = text[currency]
        from_amount = amount
        to_amount = get_amount(currency, from_amount)
        if currency in ['DOLLAR to BTC', 'DOLLAR to ETH']:
                return f"💵 {from_amount:.0f}<b>{cur[0]}</b> = {to_amount:.6f}<b>{cur[1]}</b>"
        else:
                return f"💵 {from_amount:.0f}<b>{cur[0]}</b> = {to_amount:.1f}<b>{cur[1]}</b>"
