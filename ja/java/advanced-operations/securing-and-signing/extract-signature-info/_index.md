---
title: 画像と署名情報の抽出
linktitle: 画像と署名情報の抽出
type: docs
weight: 30
url: /ja/java/extract-image-and-signature-information/
description: Java の SignatureField クラスを使用して、署名フィールドから画像を抽出し、署名情報を抽出することができます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 署名フィールドから画像を抽出する

Aspose.PDF for Java は、[SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) クラスを使用して PDF ファイルにデジタル署名する機能をサポートしており、ドキュメントに署名する際に、SignatureAppearance のための画像を設定することもできます。現在、この API は、署名フィールドに関連付けられた画像と同様に署名情報を抽出する機能も提供しています。

署名情報を抽出するために、[SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) クラスに [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) メソッドを導入しました。
 以下のコードスニペットは、SignatureFieldオブジェクトから画像を抽出する手順を示しています:

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### 署名画像の置き換え

PDFファイル内の既存の署名フィールドの画像のみを置き換える必要がある場合があります。この要件を達成するためには、まずPDFファイル内のフォームフィールドを検索し、署名フィールドを特定し、署名フィールドの寸法（矩形寸法）を取得し、同じ寸法上に画像をスタンプする必要があります。

## 署名情報の抽出

Aspose.PDF for Javaは、[SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) クラスを使用してPDFファイルにデジタル署名を行う機能をサポートしています。現在、証明書の有効性を判断することはできますが、証明書全体を抽出することはできません。抽出可能な情報には、公開鍵、サムプリント、発行者などがあります。

署名情報を抽出するために、[SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) クラスに [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) メソッドを導入しました。
 以下のコードスニペットは、SignatureFieldオブジェクトから証明書を抽出する手順を示しています:

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```