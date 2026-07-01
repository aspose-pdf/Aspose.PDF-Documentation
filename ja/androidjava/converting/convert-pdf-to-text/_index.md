---
title: PDF をテキストに変換
linktitle: PDF をテキストに変換
type: docs
weight: 120
url: /ja/androidjava/convert-pdf-to-txt/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java を使用すると、PDF ドキュメント全体をテキストファイルに変換したり、PDF のページだけをテキストファイルに変換したりできます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

オンラインでお試しください。Aspose.PDF の変換品質を確認し、結果をオンラインでこのリンクから表示できます。 [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## PDFページをテキストファイルに変換する

Aspose.PDF for Android via Java を使用して PDF ドキュメントを TXT ファイルに変換できます。Visit メソッドの [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) このタスクを解決するためのクラスです。

以下のコードスニペットは、特定のページからテキストを抽出する方法を説明しています。

```java
public void convertPDFPagesToTXT() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // Save the extracted text in text file
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

