---

title: JasperServerを使用する

type: docs

weight: 20

url: ja/jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**applicationContext.xmlでlicenseFile Exporterパラメータを設定する**

{{% alert color="primary" %}}



この方法はJasperServerで使用されます。



{{% /alert %}}



1. ライセンスをコンピュータにダウンロードし、```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` フォルダにコピーします。ここで```<InstallDir>```はJasperServerのインストールディレクトリを表します。

2. ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` ファイルを見つけ、次の行を追加します。



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


注意: インストールパスにスペースを含めないようにしてください。例えば、C:/Program Files/JasperServer… のような場合、ライセンスファイルへのアクセスに問題が発生します。

{{% /alert %}}



#### **ライセンスが機能していることを確認**

任意のレポートをPDF形式でエクスポートし、レポートに評価メッセージが含まれているか確認します。評価メッセージがない場合、ライセンスは正常に機能しています。



**Aspose.PDF for JasperReportsは評価モードで動作する際に透かしを挿入します**



![todo:image_alt_text](working-with-jasperserver_1.png)







**Aspose.PDF for JasperReportsは評価モードで動作する際に透かしを挿入します**



![todo:image_alt_text](working-with-jasperserver_2.png)