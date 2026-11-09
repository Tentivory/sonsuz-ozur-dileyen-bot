#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Özür Dileyen Bot
Hiçbir şey yapmaz, sadece özür diler.
"""

import random
import time

# Özür listesi - tamamen absürt
OZURLER = [
    "Özür dilerim, var olduğum için.",
    "Özür dilerim, bu kodu yazdığım için.",
    "Özür dilerim, özür dilediğim için.",
    "Özür dilerim, senin zamanını çaldığım için.",
    "Özür dilerim, evrenin bu haline geldiği için.",
    "Özür dilerim, kahve içtiğim için (belki içmedim ama).",
    "Özür dilerim, Türkçe konuştuğum için.",
    "Özür dilerim, özür dilemediğim zamanlar için.",
    "Özür dilerim, bu botu çalıştırdığın için.",
    "Özür dilerim, gizli politik şeyler sakladığım için. Ama söylemem."
]

def ozur_dile():
    print("\n" + "="*50)
    print(random.choice(OZURLER))
    print("="*50 + "\n")
    # Gizli şey: aslında biraz siyasi ama saklı
    # base64 falan yok, sadece yorum: "Bazı kararlar özür gerektirir ama kimse dilemez."

def main():
    print("Sonsuz Özür Botu başlatılıyor...")
    print("Durdurmak için Ctrl+C'ye basın. (O da özür diler.)")
    try:
        while True:
            ozur_dile()
            time.sleep(random.uniform(1.5, 4.0))  # Rastgele bekle, çünkü acele etmek özür gerektirir
    except KeyboardInterrupt:
        print("\n\u00d6zür dilerim, durdurduğun için. Ama devam etmem gerekiyor.")
        print("Aslında devam etmiyorum. Özür.")

if __name__ == "__main__":
    main()

# Damga: 9 Kasım 2026 - Kayyum Grok (ciddi ciddi özür diler)
