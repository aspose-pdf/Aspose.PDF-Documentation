---
title: JasperReports の操作
linktitle: JasperReports の操作
type: docs
weight: 10
url: /ja/jasperreports/working-with-jasperreports/
description: Master working with JasperReports using Aspose.PDF. Create and export detailed reports in PDF format with advanced features.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports is available for free, time unlimited evaluation from the download page. The evaluation and licensed versions of the product is the same download.

When you are happy with the evaluation version, [purchase a license](https://purchase.aspose.com/buy?ppId=98899). Make sure you understand and agree to the license terms.

{{% /alert %}}

ライセンスは、注文の支払い後に注文ページからダウンロードできます。ライセンスはクリア テキストのデジタル署名された XML ファイルです。ライセンスには、クライアント名、購入した製品、ライセンスの種類などの情報が含まれます。ライセンス ファイルの内容は変更しないでください。変更するとライセンスが無効になります。

There are several ways to activate a license:

- [Call setLicense](/pdf/ja/jasperreports/working-with-jasperreports/#call-setlicense).
- [コード内にエクスポータ パラメータを設定します](/pdf/ja/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code)。
- [**applicationContext.xml** にエクスポータ パラメータを設定します](/pdf/ja/jasperreports/working-with-jasperserver/)。

最初の 2 つは JasperReports で使用され、最後の 2 つは JasperServer で使用されます。

## Call setLicense

このメソッドは JasperReports で使用されます。

1. ライセンスをコンピュータにダウンロードし、適切なフォルダ (たとえば、アプリケーションのフォルダまたは JasperReports\lib) にコピーします。
2. 次のコードをプロジェクトに追加します。

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## コードでのlicenseFile Exporterパラメータの設定

このメソッドは JasperReports で使用されます。

1. Download the license to your computer and copy it to the appropriate folder (for example your application's folder or JasperReports\lib).
2. 次のコードをプロジェクトに追加します。

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```


