# Horspool Algoritması

Horspool algoritması, bir metin içinde belirli bir desenin varlığını tespit etmek için kullanılan bir dize eşleme (<span style ="color: red">arama</span>) algoritmasıdır. Bu algoritma, karakter dizileri arasında hızlı bir arama sağlar ve özellikle kısa desenlerde çok etkilidir. Ayrıca, Boyer-Moore algoritmasının basitleştirilmiş bir versiyonudur.

Algortima arama metnini soldan sağa, aranacak patterini sağdan sola tarar.
Yani metni ve patterni alt alta koyduktan sonra, patterin son harfinin denk geldiği eleman ile uyuşup uyuşmadığını kontrol ederek çalışır.
<pre>
- En kötü durum: Horspool algoritmasının en kötü durum zaman karmaşıklığı, desenin metnin son karakterinde bulunması durumunda O(mn) dir.
Burada n, metnin uzunluğu ve m, desenin uzunluğudur.
- En iyi durum: Horspool algoritmasının en iyi durum zaman karmaşıklığı, eşleşen bir karakter bulunduğunda deseni bir karakter atlayarak ilerleyebildiği durumdur. 
Bu durumda zaman karmaşıklığı O(n) dir.
- Ortalama durum: Horspool algoritması ortalama durumda O(m + n) zaman karmaşıklığına sahiptir.

Horspool algoritması, genellikle diğer string arama algoritmalarına göre daha hızlı çalışır ve boyutu büyük metinlerde daha iyi performans gösterir.
Ancak, en kötü durumda zaman karmaşıklığı yüksek olabilir ve bu nedenle bazı durumlarda diğer algoritmalar daha iyi performans gösterebilir.
</pre>
Burada bilmemiz gereken bir diğer önemli nokta ise bu algoritmanın sahip olduğu bad-match atlama tablosudur. Bu tablo arama esnasında atlamalar yaparak aramanın çok daha hızlı olmasını ve gereksiz kontrollerden kaçınılmasını sağlar.

## Bad-match table oluşturmak
Bunun için en çok kullanılan örneklerden biri ile başlayalım. Diyelim ki aranacak kelimemiz yani pattern'ımız TOOTH olsun.
1) Öncelikle pattern 0'dan başlayarak indexlenir<br>
    T -> 0<br>
    O -> 1<br>
    O -> 2<br>
    T -> 3<br>
    H -> 4<br>
2) Patternin uzunluğu belirlenir.<br>
length = 5<br>
3) Daha sonra TOOTH patterninin her bir elemanı gezilerek bir dictionary'de key -> value olarak saklanır.<br>
Burada her bir keyin T,O,O,T,H'un harfleri olduğu açık<br>
Her bir value ise pattern'in uzunluğundan, ilgili keyin index numarası ve 1 çıkartılması ile elde edilir.<br>
Sırayla her birinin eşleştirilmesini sağlayalım : <br>
Formül = length - index(key) - 1 <br>
4) Dikkat edilmesi gereken nokta eğer ki eleman kendini tekrar ediyorsa tekrar eden değer için yapılan hesaplama sonucu o value'nun üzerine yazılır.<br> 
5) Dikkat edilmesi gereken bir diğer nokta ise son elemana gelindiğinde bu elemana daha önce value ataması yapılmadıysa (yani pattern içinde yalnızca bir tane var ise ve bu da patternin sonunda ise) bunun değeri length'e eşitlenir. Eğer patternda daha önce geçtiyse yani value atandıysa o değer değiştirilmez.<br> 
6) Pattern'da bulunmayan harfler bad match table içerisinde * işareti ile temsil edilir ve value'ları length'e eşitlenir.<br>
<hr>
<span style="color: red">Not:</span> <i>Bad-match table içindeki value değerleri >= 1 olmalıdır! Asla negatif ya da 0 çıkmaz hata yapıp yapmadığınızı kontrol etmek için bu durumu göz önüne alabilirsiniz.</i>
<hr>

## Örnek
Öncelikle TOOTH patterni için bad match tablosunu oluşturalım<br>
<span style = "color: blue">Kural 1: </span>Formül = length - index - 1<br>
<span style = "color: blue">Kural 2: </span>Eğer aynı harf tekrar geçerse üzerine yaz<br>
<span style = "color: blue">Kural 3: </span>Eğer son harf daha önce geçmiyorsa indexi length'e eşit. Geçiyorsa hesaplanan değer korunur.
<pre>
T -> 5 - 0 - 1 = 4 (T değeri 4)
O -> 5 - 1 - 1 = 3 (O değeri 3)
O -> 5 - 2 - 1 = 2 (O nun yeni değeri 2 (II. Kural))
T -> 5 - 3 - 1 = 1 ((T nun yeni değeri 1 (II. Kural)))
H -> 5 (Daha önce geçmiyor değeri length'e eşit (III. Kural))
</pre>

Buna göre bad-match tablomuz : 
<pre>
bad_match = {
    'T' : 1,
    'O' : 2,
    'H' : 5,
    '*' : 5,
}
</pre>
<span style="color:red"></span>
Şimdi bu tablo nasıl kullanılır? Örnek olması açısından kısa bir Text'te bu TOOTH'u arayalım. <br>
Text = "TRUSTHARDTOOTHBRUSHES" olsun.
1) text ve patterin'i alt alta koyuyoruz.
<pre>
TRUSTHARDTOOTHBRUSHES
TOOTH
</pre>
2) patterin son elemanının text'te denk geldiği harf'e bakıyoruz. Bu iki harfi kıyaslıyoruz. T == H midir? Hayır. O halde bad_match table'daki T'ye denk gelen value kadar pattern'i sağa kaydırıyoruz. T'nin değeri nedir? 1. O halde 1 birim sağa.
<pre>
TRUS<span style="color:red">T</span>HARDTOOTHBRUSHES
TOOT<span style="color:red">H</span>
</pre>
3) Şimdi denk gelen harfleri tekrar kontrol ediyoruz H == H midir? Evet. O halde bir soldakileri kontrol etmeliyiz.
<pre>
TRUST<span style="color:greenyellow">H</span>ARDTOOTHBRUSHES
 TOOT<span style="color:greenyellow">H</span>
</pre>
4)  T == T midir? Evet. O halde bir soldakileri kontrol etmeliyiz.
<pre>
TRUS<span style="color:red">T</span><span style="color:greenyellow">H</span>ARDTOOTHBRUSHES
 TOO<span style="color:red">T</span><span style="color:greenyellow">H</span>
</pre>
5) S == O mudur? hayır. O halde patternla denk gelen en sondaki harf hangisiydi? H. H'nin bad_match'teki değeri nedir? 5. O halde 5 birim sağa kaydırmalıyız.
<pre>
TRU<span style="color:red">S</span><span style="color:greenyellow">T</span><span style="color:greenyellow">H</span>ARDTOOTHBRUSHES
 TO<span style="color:red">O</span><span style="color:greenyellow">T</span><span style="color:greenyellow">H</span>
</pre>
6) D == O mudur? hayır. O halde patternla denk gelen en sondaki harf hangisi? O. O'nun bad_match'teki değeri nedir? 2. O halde 2 birim sağa kaydırmalıyız.
<pre>
TRUSTHARDT<span style="color: red">O</span>OTHBRUSHES
      TOOT<span style="color: red">H</span>
</pre>
7) D == T midir? hayır. O halde patternla denk gelen en sondaki harf hangisi? T. T'nin bad_match'teki değeri nedir? 1. O halde 1 birim sağa kaydırmalıyız.
<pre>
TRUSTHARDTOO<span style="color: red">T</span>HBRUSHES
        TOOT<span style="color: red">H</span>
</pre>
8) T == T midir? evet. O halde bir soldakini kontrol edelim. (kontrol < length olduğu ve true olduğu sürece devam eder)
<pre>
TRUSTHARDTOOT<span style="color: red">H</span>HBRUSHES
         TOOT<span style="color: red">H</span>
</pre>
9) Harfler denk midir? evet. O halde bir soldakini kontrol edelim.
<pre>
TRUSTHARDTOO<span style="color: red">T</span><span style="color: greenyellow">H</span>HBRUSHES
         TOO<span style="color: red">T</span><span style="color: greenyellow">H</span>
</pre>

10) Harfler denk midir? evet. O halde bir soldakini kontrol edelim. 
<pre>
TRUSTHARDTO<span style="color: red">O</span><span style="color: greenyellow">TH</span>HBRUSHES
         TO<span style="color: red">O</span><span style="color: greenyellow">TH</span>
</pre>
11) Harfler denk midir? evet. O halde bir soldakini kontrol edelim.
<pre>
TRUSTHARDT<span style="color: red">O</span><span style="color: greenyellow">OTH</span>HBRUSHES
         T<span style="color: red">O</span><span style="color: greenyellow">OTH</span>
</pre>

12) Harfler denk midir? evet. O halde bir soldakini kontrol edelim.
<pre>
TRUSTHARD<span style="color: red">T</span><span style="color: greenyellow">OOTH</span>HBRUSHES
         <span style="color: red">T</span><span style="color: greenyellow">OOTH</span>
</pre>

13) Bir tur daha kontrol edilmesi Kontrol < length'i sağlamaz demek ki eşleşme tamamlandı!
<pre>
TRUSTHARD<span style="color: greenyellow">TOOTH</span>HBRUSHES
         <span style="color: greenyellow">TOOTH</span>
</pre>

14) Bundan sonrasında ise uzunluk kadar kaydırırlır ve aynı işlem tekrarlanır. Peki ne zamana kadar? Şimdiye kadar yapılan karşılaştırma sayısı Text'in eleman sayısından <= 5 küçük olduğu sürece devam edilir.
<pre>
TRUSTHARDTOOTHBRUS<span style="color: red">H</span>ES
              TOOT<span style="color: red">H</span>
</pre>