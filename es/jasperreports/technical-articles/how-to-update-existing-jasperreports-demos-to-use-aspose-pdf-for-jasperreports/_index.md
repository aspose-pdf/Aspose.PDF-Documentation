---
title: Cómo actualizar las demostraciones existentes de JasperReports para usar Aspose.PDF for JasperReports
linktitle: Cómo: actualizar las demostraciones existentes de JasperReports para usar Aspose.PDF for JasperReports
type: docs
weight: 20
url: /es/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Learn how to update existing JasperReports demos to leverage the capabilities of Aspose.PDF for JasperReports.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReportsincluye una serie de proyectos de demostración para ayudarle a comenzar a exportar informes a PDF. Estas demostraciones se basan en demostraciones estándar de JasperReports que se han modificado para demostrar cómo utilizar nuevos exportadores. Este tutorial recorre los pasos necesarios para actualizar las demostraciones de JasperReports existentes para usar Aspose.PDF for JasperReports.

{{% /alert %}}

## Actualización de demostraciones para usar Aspose.PDF

{{% alert color="primary" %}}

Los siguientes pasos explican cómo actualizar demostraciones existentes para usar Aspose.PDF para la extensión de exportación de JasperReports en lugar de usar la función de exportación de PDF estándar de JasperReport.

1. Descargue JasperReports de <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Make sure to download the entire archived project with the source code and demos, not just a single JAR. This tutorial was prepared using JasperReports-3.5.2.
2. Unpack the archived project to some location on your hard disk, for example C:\.
3. Copy **aspose.pdf.jasperreports.jar** from the \lib folder in **Aspose.PDF.JasperReports.zip** to ```<InstallDir>```\jasperreports\lib.
4. Abra ```<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>``` es la ubicación donde descomprimió JasperReports) para actualizar una demostración existente. Si ha seleccionado la demostración de fuentes, por ejemplo, para usar con Aspose.PDF for JasperReports, cree una copia para que la demostración original siga siendo la misma. A los efectos de este ejemplo, hemos denominado la nueva carpeta **fonts.ap**.
Nota: las demostraciones se ejecutarán desde ```<InstallDir>``` \jasperreports\demo\samples porque los scripts de compilación de demostración se basan en la estructura de carpetas de JasperReports. Si cambia la carpeta de muestra, debe modificar los scripts de compilación.
5. Abra el archivo **FontsApp.java** de la carpeta src y agregue una referencia a Aspose.PDF for JasperReports:
   import com.aspose.pdf.jr3_7_0.jasperreports.*;
   (Estamos usando jr3_7_0 porque este tutorial se preparó con JasperReports 3.5.2).
6. Añade una nueva cadena:
   Cadena final estática privada TASK_ASPOSE_PDF = "aspose_pdf"; junto con las variables existentes como una opción de exportación a través de Aspose.PDF for JasperReports.
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
10. Make a copy of the following segment and place it inside the same file:

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
   - Unpack the ANT tool and set up environment variables as described in the tool's manual.
   -  Change the current directory to <InstallDir>\demo\hsqldb and run the following command line:
      servidor de ejecución de hormigas
12. Abra una nueva instancia del símbolo del sistema y cambie el directorio actual a <InstallDir>\demo\samples\fonts.ap y ejecute los siguientes comandos en la línea de comando:
13. ant javac: para compilar los archivos fuente Java de la aplicación de prueba
14. compilación ant: para compilar el diseño del informe XML y producir el archivo .jasper
15. relleno de hormiga: para llenar el diseño del informe compilado con datos y producir el archivo .jrprint
16. ant aspose_ pdf: para producir un archivo PDF usando Aspose.PDF for JasperReports.
17. Abra el PDF resultante (**FontsReport.pdf**) de la carpeta <InstallDir>\demo\samples\ fonts.ap\build\reports\.

{{% /alert %}}


