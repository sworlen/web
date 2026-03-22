"""Zadání: Procvičování základů Pythonu na receptu na lasagne."""

# 1. Definice konstanty pro očekávaný čas pečení (40 minut)
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Vypočítá zbývající čas pečení v minutách.

    :param elapsed_bake_time: int - kolik minut už jsou lasagne v troubě.
    :return: int - kolik minut ještě zbývá do konce pečení.

    Tato funkce vezme očekávaný čas (40) a odečte od něj čas, 
    který už lasagne v troubě strávily.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Vypočítá čas přípravy podle počtu vrstev.

    :param number_of_layers: int - počet vrstev lasagní.
    :return: int - celkový čas přípravy (každá vrstva = 2 minuty).
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Vypočítá celkový čas strávený vařením (příprava + pečení).

    :param number_of_layers: int - počet vrstev lasagní.
    :param elapsed_bake_time: int - kolik minut už se lasagne pečou.
    :return: int - celkový součet minut strávených v kuchyni.

    Tato funkce sčítá čas potřebný na přípravu vrstev a čas, 
    který už lasagne strávily pečením v troubě.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time