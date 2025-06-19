# DejaView

## Proje Hakkında

**DejaView**, etiketlenmemiş (labelsız) haber metinlerini otomatik olarak sınıflandırmak ve bu haberler üzerinde hiyerarşik bir kümeleme (clustering) gerçekleştirmek amacıyla geliştirilmiş bir projedir. 

Bu projede farklı kümeleme algoritmaları kullanılarak haberlerin kategorilere ayrılması hedeflenmektedir. Böylece, büyük veri kümeleri içinde anlamlı gruplar oluşturularak veri analizi ve keşif süreçleri kolaylaştırılabilir.

---

## Kullanılan Veri

- Veri dosyası: `Data/data.csv`
- İçerik: Haber metinleri
- Kolonlar: `category` (etiket), `title` (başlık), `content` (haber içeriği)

---

## Kullanılan Algoritmalar

Projede aşağıdaki kümeleme algoritmaları kullanılmıştır:

- **K-Means Clustering**
- **Agglomerative Clustering** (Hiyerarşik Kümeleme)
- **GMM** (Gauss Karışım Modeli)
- **OPTICS** (Yoğunluk Tabanlı Kümeleme Alternatifi)
- **Mean Shift algorithm** (Ortalama Kaydırma Algoritması)

Bu algoritmaların her biri farklı özelliklere ve avantajlara sahiptir. Projede performans ve doğruluk karşılaştırmaları yapılmaktadır.

| Özellik                       | K-Means        | GMM              | Agglomerative      | OPTICS             | Mean Shift              |
| ----------------------------- | -------------- | ---------------- | ------------------ | ------------------ | ----------------------- |
| **Küme sayısı gerekli mi?**   | ✅ Evet         | ✅ Evet           | ❌ Hayır            | ❌ Hayır            | ❌ Hayır                 |
| **Küme şekli varsayımı**      | Küresel        | Eliptik          | Esnek (hiyerarşik) | Serbest (yoğunluk) | Serbest (mod yoğunluğu) |
| **Yumuşak atama?**            | ❌ Hayır        | ✅ Evet           | ❌ Hayır            | ❌ Hayır            | ❌ Hayır                 |
| **Aykırı değer algılar mı?**  | ❌ Hayır        | ⚠️ Kısmen        | ❌ Hayır            | ✅ Evet             | ⚠️ Sınırlı              |
| **Büyük veri için uygun mu?** | ✅ Evet         | ⚠️ Orta          | ❌ Zorlanır         | ⚠️ Orta-yavaş      | ❌ Yavaş                 |
| **Parametre hassasiyeti**     | ✅ Çok          | ✅ Çok            | ⚠️ Orta            | ✅ Az               | ⚠️ Bandwidth kritik     |
| **Yöntem tipi**               | Merkez tabanlı | Olasılık tabanlı | Hiyerarşik         | Yoğunluk tabanlı   | Yoğunluk / mod arama    |



---

## Proje Dosya Yapısı
```bash
DejaView/
│
├── Datas/
│ └── data.csv # Veri dosyası
│ └── scrape/
│
├── Extras/ # Ekstra Notebooklar
│
├── Notebooks/
│ ├── agglomerative_clustering.ipynb
│ ├── gmm_model.ipynb
│ ├── kmeans_clustering.ipynb
│ ├── mean_shift_model.ipynb
│ └── optics_clustering.ipynb
│
├── Models/ # Eğitim sonrası modellerin saklandığı klasör
│
├── Utils/ # Veri ön işleme ve yardımcı fonksiyonlar
│
└── README.md # Proje açıklaması ve kullanım
```


## Kurulum ve Kullanım

- Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```
- Veri dosyasını Data/data.csv dizinine yerleştirin.

- İlgili .ipynb dosyasını açarak adım adım analiz ve kümeleme işlemlerini yapabilirsiniz.

- Her notebook'ta farklı algoritmaların uygulanması ve sonuçların karşılaştırılması bulunmaktadır.
