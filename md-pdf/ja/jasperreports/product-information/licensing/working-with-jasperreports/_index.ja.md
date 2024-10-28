---

title: Working with JasperReports

type: docs

weight: 10

url: /jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



Aspose.Words for JasperReportsは、ダウンロードページから無料で、時間無制限の評価版を利用できます。製品の評価版とライセンス版は同じダウンロードです。



評価版に満足したら、[ライセンスを購入](http://www.aspose.com/purchase/default.aspx)してください。ライセンス条件を理解し、同意することを確認してください。



{{% /alert %}}



ライセンスは、注文が支払われた後、注文ページからダウンロードできます。ライセンスはクリアテキストの、デジタル署名されたXMLファイルです。ライセンスには、クライアント名、購入した製品、ライセンスタイプなどの情報が含まれています。ライセンスファイルの内容を変更しないでください。ライセンスが無効になります。



ライセンスをアクティブにする方法はいくつかあります:



- [setLicenseを呼び出す](/pdf/jasperreports/working-with-jasperreports/#call-setlicense)。


- [コード内でエクスポーターパラメータを設定する](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code)。

- [**applicationContext.xml** にエクスポーターパラメータを設定する](/pdf/jasperreports/working-with-jasperserver/)。

最初の2つはJasperReportsで使用され、最後のものはJasperServerで使用されます。

#### **setLicenseを呼び出す**

<ins> **この方法はJasperReportsで使用されます。**

1. ライセンスをコンピュータにダウンロードし、適切なフォルダ（例えばアプリケーションフォルダやJasperReports\lib）にコピーします。

2. 以下のコードをプロジェクトに追加します：

```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // ライセンスファイルを含むストリームオブジェクトを作成

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // ストリームオブジェクトを通してライセンスを設定

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}

```

#### **コード内でlicenseFileエクスポーターパラメータを設定する**

<ins> **この方法はJasperReportsで使用されます。**

1. ダウンロードしたライセンスをコンピュータに保存し、適切なフォルダ（例えば、アプリケーションのフォルダやJasperReports\lib）にコピーしてください。

2. 次のコードをプロジェクトに追加します：