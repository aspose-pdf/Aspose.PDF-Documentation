---

title: 使用 JasperReports

type: docs

weight: 10

url: /jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Aspose.Words for JasperReports 可以从下载页面免费获取，且无时间限制。产品的评估版和授权版是相同的下载。

当您对评估版满意时，[购买许可证](http://www.aspose.com/purchase/default.aspx)。确保您理解并同意许可证条款。

{{% /alert %}}

许可证可在订单支付后从订单页面下载。许可证是一个明文、数字签名的 XML 文件。许可证包含信息，例如客户名称、购买的产品和许可证类型。不要修改许可证文件的内容：这会使许可证无效。

有几种方法可以激活许可证：

- [调用 setLicense](/pdf/jasperreports/working-with-jasperreports/#call-setlicense)。

- [在代码中设置导出参数](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code)。

- [在 **applicationContext.xml** 中设置导出参数](/pdf/jasperreports/working-with-jasperserver/)。

前两个用于 JasperReports，最后一个用于 JasperServer。

#### **调用 setLicense**

<ins> **此方法用于 JasperReports。**

1. 下载许可证到您的计算机并将其复制到适当的文件夹（例如您的应用程序文件夹或 JasperReports\lib）。

2. 将以下代码添加到您的项目中：

```
import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // 创建一个包含许可证文件的流对象

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // 通过流对象设置许可证

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}

```

#### **在代码中设置 licenseFile 导出参数**

<ins> **此方法用于 JasperReports。**

1. 下载许可证到您的计算机，并将其复制到相应的文件夹（例如，您的应用程序文件夹或 JasperReports\lib）。

2. 将以下代码添加到您的项目中：



```



import com.aspose.pdf.jr3_7_0.jasperreports.*;



com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.exportReport();



```