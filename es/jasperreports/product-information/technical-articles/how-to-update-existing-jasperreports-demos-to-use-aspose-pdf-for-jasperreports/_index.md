---
title: Cómo - Actualizar demos existentes de JasperReports para usar Aspose.Pdf para JasperReports
type: docs
weight: 20
url: es/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para JasperReports incluye una serie de proyectos de demostración para ayudarte a comenzar a exportar informes a PDF. Estas demostraciones se basan en las demostraciones estándar de JasperReports que han sido modificadas para demostrar cómo usar los nuevos exportadores. Este tutorial, pasa por los pasos requeridos para actualizar las demostraciones existentes de JasperReports para usar Aspose.PDF para JasperReports.

{{% /alert %}}
### **Actualizando Demos para usar Aspose.PDF**

{{% alert color="primary" %}}

Los siguientes pasos explican cómo actualizar las demostraciones existentes para usar la extensión de exportación de Aspose.PDF para JasperReports en lugar de usar la función de exportación estándar a PDF de JasperReport.
{{% /alert %}}

1. Descarga JasperReports desde <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Asegúrate de descargar el proyecto archivado completo con el código fuente y las demostraciones, no solo un único JAR. Este tutorial fue preparado utilizando JasperReports-3.5.2.  
2. Desempaqueta el proyecto archivado en alguna ubicación en tu disco duro, por ejemplo C:\.  
3. Copia **aspose.pdf.jasperreports.jar** desde la carpeta \lib en **Aspose.PDF.JasperReports.zip** a ```<InstallDir>```\jasperreports\lib.  
4. Abre ```<InstallDir>```\jasperreports\demo\samples, (donde ```<InstallDir>``` es la ubicación donde has desempaquetado JasperReports) para actualizar un demo existente. Si has seleccionado el demo de fuentes, por ejemplo, para usar con Aspose.PDF para JasperReports, crea una copia de este para que el demo original permanezca igual. Para el propósito de este ejemplo, hemos nombrado la nueva carpeta **fonts.ap**.  
Nota: los demos se ejecutarán desde ```<InstallDir>``` \jasperreports\demo\samples porque los scripts de construcción de los demos dependen de la estructura de carpetas de JasperReports. Si cambias la carpeta de muestra, tienes que modificar los scripts de construcción.  
5. Abre el archivo **FontsApp.java** desde la carpeta src y añade una referencia a Aspose.PDF para JasperReports:

   import com.aspose.pdf.jr3_7_0.jasperreports.*;(Estamos usando jr3_7_0 porque este tutorial fue preparado con JasperReports 3.5.2.)
6. Añadir una nueva cadena:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; junto con las variables existentes como una opción de exportación a través de Aspose.PDF para JasperReports.
7. Localizar el segmento de código else if (TASK_PDF.equals(taskName)) y copiar todo el segmento.
8. Pegar el fragmento de código bajo el mismo segmento.

```
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
  System.err.println("Tiempo de creación del PDF : " + (System.currentTimeMillis() - start));
}
```

```
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
9. Abre el archivo **build.xml**.
10. Haz una copia del siguiente segmento y colócalo dentro del mismo archivo:

```
 <target name="pdf" description="Generar PDF vía Aspose.PDF para JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. Para ejecutar la demo:

   -  Descargue la herramienta ANT de <http://ant.apache.org/bindownload.cgi>.
- Desempaqueta la herramienta ANT y configura las variables de entorno como se describe en el manual de la herramienta.
- Cambia el directorio actual a <InstallDir>\demo\hsqldb y ejecuta la siguiente línea de comando:
  ant runServer
12. Abre una nueva instancia de la línea de comandos y cambia el directorio actual a <InstallDir>\demo\samples\fonts.ap y ejecuta los siguientes comandos en la línea de comandos:
13. ant javac – para compilar los archivos fuente de Java de la aplicación de prueba
14. ant compile – para compilar el diseño del informe XML y producir el archivo .jasper
15. ant fill – para llenar el diseño del informe compilado con datos y producir el archivo .jrprint
16. ant aspose_ pdf – para producir un archivo PDF usando Aspose.PDF para JasperReports.
17. Abre el archivo PDF resultante (**FontsReport.pdf**) desde la carpeta <InstallDir>\demo\samples\fonts.ap\build\reports\.