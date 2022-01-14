from colorama import Fore


def pagarme_mission():
    return "Empoderar os negócios digitais do empreendedor Brasileiro."


def pagarme():
    return r"""Pagarme"""


if __name__ == "__main__":
    print(f"{Fore.BLUE} Qual é a missão da")
    print(f"{Fore.GREEN} {pagarme()} ?")
    print(f"{Fore.BLUE} {pagarme_mission()}")
