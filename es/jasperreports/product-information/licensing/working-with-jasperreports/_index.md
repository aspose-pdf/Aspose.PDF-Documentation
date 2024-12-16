---

title: Trabajando con JasperReports

type: docs

weight: 10

url: /es/jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



Aspose.Words para JasperReports está disponible para evaluación gratuita e ilimitada en el tiempo desde la página de descarga. Las versiones de evaluación y con licencia del producto son la misma descarga.



Cuando esté satisfecho con la versión de evaluación, [compre una licencia](http://www.aspose.com/purchase/default.aspx). Asegúrese de entender y aceptar los términos de la licencia.



{{% /alert %}}



La licencia está disponible para su descarga desde la página de pedido después de que se haya pagado el pedido. La licencia es un archivo XML firmado digitalmente y en texto claro. La licencia contiene información como el nombre del cliente, el producto comprado y el tipo de licencia. No modifique el contenido del archivo de licencia: invalida la licencia.



Hay varias formas de activar una licencia:



- [Llame a setLicense](/pdf/es/jasperreports/working-with-jasperreports/#call-setlicense).


- [Establezca un parámetro de exportador en el código](/pdf/es/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).

- [Establecer un parámetro de exportador en **applicationContext.xml**](/pdf/es/jasperreports/working-with-jasperserver/).



Los dos primeros se usan con JasperReports, el último con JasperServer.

#### **Llamar a setLicense**

<ins> **Este método se utiliza con JasperReports.**



1. Descargue la licencia a su computadora y cópiela en la carpeta adecuada (por ejemplo, la carpeta de su aplicación o JasperReports\lib).

2. Agregue el siguiente código a su proyecto:



```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // crear un objeto de flujo que contenga el archivo de licencia

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  



    // Establecer la licencia a través del objeto de flujo

 

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}



```



#### **Establecer el Parámetro Exporter licenseFile en el Código**



<ins> **Este método se utiliza con JasperReports.**



1. Download la licencia a tu computadora y cópiala en la carpeta adecuada (por ejemplo, la carpeta de tu aplicación o JasperReports\lib).

2. Agrega el siguiente código a tu proyecto:



```



import com.aspose.pdf.jr3_7_0.jasperreports.*;



com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.exportReport();



```