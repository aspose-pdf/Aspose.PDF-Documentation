---
title: Cómo: actualizar las demostraciones existentes de JasperReports para usar Aspose.PDF para JasperReports
linktitle: Cómo: actualizar las demostraciones existentes de JasperReports para usar Aspose.PDF para JasperReports
type: docs
weight: 20
url: /es/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Learn how to update existing JasperReports demos to leverage the capabilities of Aspose.PDF for JasperReports.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports includes a number of demo projects to help you get started exporting reports to PDF. These demos are based on standard JasperReports demos that have been modified to demonstrate how to use new exporters. This tutorial, goes through the steps required to update the existing JasperReports demos to use Aspose.PDF for JasperReports.

{{% /alert %}}

## Updating Demos to use Aspose.PDF

{{% alert color="primary" %}}

Los siguientes pasos explican cómo actualizar demostraciones existentes para usar Aspose.PDF para la extensión de exportación de JasperReports en lugar de usar la función de exportación de PDF estándar de JasperReport.

1. Download JasperReports from <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Asegúrese de descargar todo el proyecto archivado con el código fuente y las demostraciones, no solo un JAR. Este tutorial se preparó utilizando JasperReports-3.5.2.
2. Desempaquete el proyecto archivado en alguna ubicación de su disco duro, por ejemplo C:\.
3. Copie **aspose.pdf.jasperreports.jar** de la carpeta \lib en **Aspose.PDF.JasperReports.zip** a ```<InstallDir>```\jasperreports\lib.
4. Abra ```<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>``` es la ubicación donde descomprimió JasperReports) para actualizar una demostración existente. Si ha seleccionado la demostración de fuentes, por ejemplo, para usar con Aspose.PDF para JasperReports, cree una copia para que la demostración original siga siendo la misma. A los efectos de este ejemplo, hemos denominado la nueva carpeta **fonts.ap**.
Nota: las demostraciones se ejecutarán desde ```<InstallDir>``` \jasperreports\demo\samples porque los scripts de compilación de demostración se basan en la estructura de carpetas de JasperReports. Si cambia la carpeta de muestra, debe modificar los scripts de compilación.
5. Abra el archivo **FontsApp.java** de la carpeta src y agregue una referencia a Aspose.PDF para JasperReports:
   importar com.aspose.pdf.jr3_7_0.jasperreports.*;
   (Estamos usando jr3_7_0 porque este tutorial se preparó con JasperReports 3.5.2).
6. Añade una nueva cadena:
   Cadena final estática privada TASK_ASPOSE_PDF = "aspose_pdf"; junto con las variables existentes como una opción de exportación a través de Aspose.PDF para JasperReports.
7. Localice el segmento de código for else if (TASK_PDF.equals(taskName)) y copie el segmento completo.
8. Pegue el fragmento de código debajo del mismo segmento.

```java
 else if (TASK_PDF.equals(taskName))
{
  File sourceFile = new File(fileName);
  JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
  File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");
  JRPdfExporter exporter = new JRPdfExporter();
  HashMap fontMap = new HashMap();
  FontKey key = new FontKey("DejaVu Serif", true, false);
  PdfFont font = new PdfFont("DejaVuSerif-Bold.ttf", "Cp1252", true);
  fontMap.put(key, font);
  exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);
  exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());
  exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
  exporter.exportReport();
  System.err.println("PDF creation time : " + (System.currentTimeMillis() - start));
}
```

```text
update
else if (TASK_PDF.equals(taskName))
as
else if (TASK_ASPOSE_PDF.equals(taskName))
replace
JRPdfExporter exporter = new JRPdfExporter();
with
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
```

9. Abra el archivo **build.xml**.
10. Haga una copia del siguiente segmento y colóquelo dentro del mismo archivo:

```xml
 <target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```diff
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. Para ejecutar la demostración:
   -  Descargue la herramienta ANT de <http://ant.apache.org/bindownload.cgi>.
   - Desempaquete la herramienta ANT y configure las variables de entorno como se describe en el manual de la herramienta.
   -  Cambie el directorio actual a <InstallDir>\demo\hsqldb y ejecute la siguiente línea de comando:
      servidor de ejecución de hormigas
12. Abra una nueva instancia del símbolo del sistema y cambie el directorio actual a <InstallDir>\demo\samples\fonts.ap y ejecute los siguientes comandos en la línea de comando:
13. ant javac: para compilar los archivos fuente Java de la aplicación de prueba
14. compilación ant: para compilar el diseño del informe XML y producir el archivo .jasper
15. relleno de hormiga: para llenar el diseño del informe compilado con datos y producir el archivo .jrprint
16. ant aspose_ pdf: para producir un archivo PDF usando Aspose.PDF para JasperReports.
17. Abra el PDF resultante (**FontsReport.pdf**) de la carpeta <InstallDir>\demo\samples\ fonts.ap\build\reports\.

{{% /alert %}}

