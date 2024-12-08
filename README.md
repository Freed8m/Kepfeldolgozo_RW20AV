# Egyszerűsített képfeldolgozó program<br>
Ez egy képszerkesztő program, egyszerű, gyors, és (egyenlőre) egyszeri operációkhoz.<br><br> Lényege hogy gyors legyen és kicserélje a komplexebb, de lassabb programokat ha csak épp egy egyszerű funkcióra van szükségünk.

# Jellemzők
- Egyszerű felület (Tkinter alapú)
- Megjelenített kép, egyes változások megjelenítése
- Jelenleg egyszeri operációk támogatottak
- Jelenlegi opciók
  - Forgatás (90°, 180°)
  - Kép átméretezés (Bilineáris)
  - Gauss alapú képelmosás

# Használat
### Indítás
- Python (3.0 vagy újabb) szükséges
- Terminálban vagy parancssorban futtatandó parancs:
    <br>`python kepfeldolgozo.py`
### Általános útmutató  
- A program indításkor rögtön fájlkiválasztáshoz kerülünk
- Miután a kép betölt, két fajta opció-típusról beszélhetünk:
  - A forgatás opciók rögtön exportálják a képet egy szuffixummal, rögtönzött megjelenítés nem lehetséges
  - Az átméretezés és Gauss-blur csak akkor exportálódik ha az **'Exportál?'** doboz be van pipálva
- Gauss-blur-nél lehetséges a kép megtekintése exportálás nélkül
- Az exportált kép az eredeti képpel megegyező mappába fog kerülni, az operációhoz illően hozzáadott szuffixummal

<br>*Egyenlőre többszöri, 'batch' képfeldolgozás nem lehetséges.*

# Követelmények
- Python 3.0 vagy újabb
  -   Tkinter opcionális modul a python telepítőben
