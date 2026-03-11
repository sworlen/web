# Poslední změny (pro snadné uložení na GitHub)

Tento soubor slouží jako rychlá „paměť“ posledních úprav v projektu.

## Co je hotové

- Přepnutí načítání datasetu zpět na `data.js` (místo `data.json`).
- Kompatibilita pro dataset ve stylu `const mediaData = [...]`.
- Zobrazení platforem (`platforms`) na kartách i v detailním modalu.
- Přidáno **Try my luck** + rozšířený discovery/filtrační panel.
- Trend chipy (např. nejhledanější) + lokální engagement statistiky.
- Oprava identity v sidebaru při návštěvě cizího profilu (nemění tvoje jméno/avatar).
- Přidané doporučení podobných titulů v modalu s proklikem.

## Poslední commity

- `c1159a2` Add luck/filter discovery UX and fix profile identity persistence
- `eced9c5` Fix data.js global const loading compatibility
- `99042b8` Fix data.js loading flow and show platforms in UI
- `fcb367e` Switch media bootstrap from data.json back to data.js

## Jak to uložit na GitHub

```bash
git status
git add .
git commit -m "Save latest app updates"
git push origin <tvoje-vetev>
```

Pokud už commit existuje, stačí jen:

```bash
git push origin <tvoje-vetev>
```
