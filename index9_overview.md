# Přehled souboru `index (9).html`

## Co soubor obsahuje
- Kompletní jednostránkovou webovou aplikaci „MEDIA VAULT | TITAN EDITION PRO“ (HTML + CSS + JS).
- Napojení na Firebase Authentication a Firestore (`onAuthStateChanged`, `onSnapshot`).
- Aplikační logiku v objektu `window.Core` (navigace, vyhledávání, ratingy, playlisty, modal, progress).

## Databáze funkcí
- Funkce byly uloženy do souboru `function_database_index9.json`.
- Evidováno: **28** metod `window.Core` a **2** callback funkce v module skriptu.

## Seznam metod `window.Core`
- `init()` — řádky 343-343
- `toggleSidebar(f)` — řádky 345-350
- `save()` — řádky 352-357
- `handleAuth()` — řádky 359-364
- `toggleAuthMode()` — řádky 366-371
- `logout()` — řádky 373-373
- `navigate(view, el)` — řádky 375-383
- `handleSearch(v)` — řádky 385-404
- `changePage(o)` — řádky 406-406
- `toggleFavorite(e, id)` — řádky 408-414
- `openPlaylistPicker(e, id)` — řádky 416-434
- `confirmAddToPlaylist(name)` — řádky 436-442
- `createPlaylistFromPicker()` — řádky 444-452
- `closePicker()` — řádky 454-454
- `addPlaylistPrompt()` — řádky 456-459
- `calculateProgress(item)` — řádky 461-468
- `renderGrid()` — řádky 470-513
- `openModal(id)` — řádky 515-523
- `updateModalProgress()` — řádky 525-529
- `renderStars(id)` — řádky 531-538
- `starHover(el, v)` — řádky 540-543
- `rate(id, v)` — řádky 545-551
- `toggleAccordion(el)` — řádky 553-560
- `renderContent(item)` — řádky 562-583
- `toggleEp(uid, el)` — řádky 585-591
- `deletePlaylist(e, n)` — řádky 593-599
- `syncPlaylists()` — řádky 601-607
- `closeModal()` — řádky 609-609

## Modulové callbacky
- `onAuthStateChanged_callback(user)` — řádek 301
- `onSnapshot_callback(snapshot)` — řádek 321
