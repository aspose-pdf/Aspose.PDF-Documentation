---
title: PDFをテキストに変換
linktitle: PDFをテキストに変換
type: docs
weight: 120
url: ja/androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Javaを使用して、PDFドキュメント全体をテキストファイルに変換したり、PDFページのみをテキストファイルに変換したりできます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

オンラインで試す。このリンクでAspose.PDF変換の品質を確認し、結果をオンラインで表示できます: [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## PDFページをテキストファイルに変換

Aspose.PDF for Android via Javaを使用して、PDFドキュメントをTXTファイルに変換できます。このタスクを解決するには、[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber)クラスのVisitメソッドを使用する必要があります。

次のコードスニペットは、特定のページからテキストを抽出する方法を説明しています。

```java
public void convertPDFPagesToTXT() {
        // ドキュメントを開く
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

        // 抽出したテキストをテキストファイルに保存
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