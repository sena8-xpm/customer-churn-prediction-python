# 📉 Müşteri Terk (Churn) Analizi ve Sınıflandırma Modeli

Bu proje, bir telekom şirketinin müşteri verilerini kullanarak hangi müşterilerin hizmeti bırakacağını (Churn) önceden tahmin eden bir Makine Öğrenmesi (Sınıflandırma) modelinin geliştirilmesi amacıyla hazırlanmıştır.

## 📌 Kullanılan Teknolojiler
* **Python 3.x**
* **Pandas** (Veri Düzenleme)
* **Scikit-Learn** (Decision Tree Classifier, Train-Test Split, Accuracy Metric)

## 🛠️ Uygulanan Adımlar
1. **Sınıflandırma Mantığı:** Sürekli değer tahmini yerine kategorik ($1$ = Terk Etti, $0$ = Kaldı) hedef değişken belirlendi.
2. **Model Eğitimi:** `DecisionTreeClassifier` (Karar Ağacı) algoritması kuruldu ve eğitildi.
3. **Değerlendirme:** Test seti üzerinde `Accuracy Score` ile model performansı ölçüldü.
4. **Aksiyon Odaklı Tahmin:** Şirkete yeni katılan veya davranışı değişen riskli müşteriler tespit edilerek uyarı mekanizması kurgulandı.

## 🚀 Proje Kodları
Projenin Python kodlarına [buradan](./main.py) ulaşabilirsiniz.
