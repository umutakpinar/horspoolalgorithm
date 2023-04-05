def black_match_table(
        searchPattern="TOOTH"):  # aranacak kelime bu şekilde parametre olarak verilmeli değer verilmezse TOOOTH
    pattern = list(searchPattern)
    length = len(pattern)  # patternin boyutunu aldık
    skip = [i for i in
            range(256)]  # ASCII tablsoundaki karakterlerin hepsi geçerli olsun diye 256 elemanlı bir dizi oluşturduk
    for i in skip:  # bu bizim black_match_table'ımız buradaki her bir elemanı pattern boyutuna eşitledik.
        skip[i] = length
    for i in pattern:
        if i != pattern[len(pattern) - 1]:  # patternin son elemanı hariç hepsinin değerlerini hesapladık (III. kural)
            skip[ord(i)] = length - pattern.index(
                i) - 1  # 256 karakterli dizi oluşturduğumuz için ASCII'ye dönüştürdük ord() metodu ile her birinin value'larını hesaplayıp skip tablosundaki ilgili indexlere gönderdik
    return skip  # skipi geri döndürdük bu bizim black_match_table değerimiz


def search(searchText="TRUSTHARDTOOTHBRUSHES", searchPattern="TOOTH"):
    text = list(searchText)
    pattern = list(searchPattern)
    skip = black_match_table(searchPattern)
    textSize = len(text)
    patternSize = len(pattern)

    shift = 0  # bunu değeri kadar sağa kaydırılmış olacak
    found = 0  # patternin textte kaç kere geçtiği

    while shift <= (textSize - patternSize):  # aranmayan kısım kadar arama işlemi devam edebilir.
        j = patternSize - 1  # readme dosyasındaki mantıkla pattern'ın son karakterininin index numarasını seçtik çünkü bu algoritma sondan başlayarak eşleşmeleri arıyor demiştik
        count = 0  # şimdiye kadar denenen eşleşme sayısı
        while j >= 0 and pattern[j] == text[shift + j]:  # texti ve pattern'i alt alta koyduğumuzda sağdan sola doğru eşleşme olduğu sürece ve j patternin boyundan kısa olmadığı sürece sola doğru kontrol etmeye devam et
            count = count + 1
            j = j - 1
        if j < 0:  # Eğer sıfırdan küçükse demek ki tam bir eşleşme oldu bu durumda aramaya devam etmek için patternSize kadar ilerlemeli
            found = found + 1
            shift = shift + patternSize
        else:  # demek ki j sıfırdan küçük değil bu durumda tam bir eşleşme sağlanamadı o halde şu anki karşılaştırılan harfin ASCII numarası ne ise skip dizisinde onu bulup değeri kadar sağa kaydırmalı yani
            shift = shift + skip[ord(text[shift + j + count])]

    print(found)


search()
