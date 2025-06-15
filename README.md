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
- **DBSCAN** (Yoğunluk Tabanlı Kümeleme)
- **OPTICS** (Yoğunluk Tabanlı Kümeleme Alternatifi)

Bu algoritmaların her biri farklı özelliklere ve avantajlara sahiptir. Projede performans ve doğruluk karşılaştırmaları yapılmaktadır.

---

## Proje Dosya Yapısı
```bash
DejaView/
│
├── Datas/
│ └── data.csv # Veri dosyası
| └── scrape/
│
├── Extras/ # Ekstra Notebooklar
│
├── Notebooks/
│ ├── kmeans_clustering.ipynb
│ ├── agglomerative_clustering.ipynb
│ ├── dbscan_clustering.ipynb
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