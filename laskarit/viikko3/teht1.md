```mermaid
classDiagram
    Pelilauta "1" --> "40" Ruutu
    Pelaaja "1" --> "1" Pelinappula
    Pelinappula "*" --> "1" Ruutu
    Pelinappula "2..8" --> "1" Pelilauta
    Noppa "2" --> Pelilauta
    Pelaaja "1" ..> "2" Noppa
    Ruutu "1" --> "1" Ruutu
    class Pelaaja{

    }
    class Pelilauta
    class Ruutu{
        seuraava
    }
    class Noppa
    class Pelinappula
```