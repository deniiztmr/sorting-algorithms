Merge Sort Aşamaları
1. Bölme (Divide) Aşaması:

Dizi ikiye bölünür:

ruby
Kopyala
Düzenle
[16, 21, 11, 8, 12, 22]

=> [16, 21, 11]     [8, 12, 22]

=> [16] [21, 11]    [8] [12, 22]

=> [16] [21] [11]   [8] [12] [22]


2.Birleştirme ve Sıralama Aşaması:

Şimdi sıralayarak geri birleştirilir:

Sol taraf:
csharp
Kopyala
Düzenle
[21] + [11] => [11, 21]
[16] + [11, 21] => [11, 16, 21]

Sonuç (Sıralı Hâli):
[8, 11, 12, 16, 21, 22] 
