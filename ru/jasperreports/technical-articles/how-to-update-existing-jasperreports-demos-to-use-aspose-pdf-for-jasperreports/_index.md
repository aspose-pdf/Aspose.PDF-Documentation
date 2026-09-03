---
title: Как обновить существующие демонстрации JasperReports для использования Aspose.PDF for JasperReports
linktitle: Как обновить существующие демонстрации JasperReports для использования Aspose.PDF for JasperReports
type: docs
weight: 20
url: /ru/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Узнайте, как обновить существующие демонстрационные версии JasperReports, чтобы использовать возможности Aspose.PDF for JasperReports.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports включает ряд демонстрационных проектов, которые помогут вам начать экспорт отчетов в PDF. Эти демонстрации основаны на стандартных демонстрациях JasperReports, которые были изменены, чтобы продемонстрировать, как использовать новые средства экспорта. В этом руководстве описаны шаги, необходимые для обновления существующих демонстраций JasperReports для использования Aspose.PDF for JasperReports.

{{% /alert %}}

## Обновите демонстрации для использования Aspose.PDF

{{% alert color="primary" %}}

Следующие шаги объясняют, как обновить существующие демонстрационные версии для использования Aspose.PDF для расширения экспорта JasperReports вместо использования стандартной функции экспорта PDF JasperReport.

1. Загрузите JasperReports с сайта <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Обязательно загрузите весь заархивированный проект с исходным кодом и демонстрациями, а не только один JAR-файл. Это руководство было подготовлено с использованием JasperReports-3.5.2.
2. Распакуйте заархивированный проект в какое-нибудь место на жестком диске, например C:\.
3. Скопируйте **Aspose.PDF.jasperreports.jar** из папки \lib в **Aspose.PDF.JasperReports.zip** в ```<InstallDir>```\jasperreports\lib.
4. Откройте ```<InstallDir>```\jasperreports\demo\samples, где ```<InstallDir>``` — это каталог, в который вы распаковали JasperReports, чтобы обновить существующую демонстрацию. Если вы выбрали, например, демонстрацию шрифтов для использования с Aspose.PDF for JasperReports, создайте ее копию, чтобы исходная демонстрация осталась без изменений. В этом примере новая папка называется **fonts.ap**.
Примечание. Демоверсии будут запускаться из ```<InstallDir>``` \jasperreports\demo\samples, поскольку сценарии сборки демо основаны на структуре папок JasperReports. Если вы измените папку с образцами, вам придется изменить сценарии сборки.
5. Откройте файл **FontsApp.java** из папки src и добавьте ссылку на Aspose.PDF for JasperReports:
   `import com.Aspose.PDF.jr3_7_0.jasperreports.*;`
   (Мы используем jr3_7_0, поскольку это руководство было подготовлено с использованием JasperReports 3.5.2.)
6. Добавьте новую строку:
   `private static final String TASK_ASPOSE_PDF = "aspose_pdf";`
   Добавьте эту строку рядом с существующими переменными как параметр экспорта через Aspose.PDF for JasperReports.
7. Найдите сегмент кода for else if (TASK_PDF.equals(taskName)) и скопируйте его целиком.
8. Вставьте фрагмент кода в тот же сегмент.

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
com.Aspose.PDF.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.Aspose.PDF.jr3_7_0.jasperreports.JrPdfExporter();
```

9. Откройте файл **build.xml**.
10. Сделайте копию следующего сегмента и поместите его в тот же файл:

```xml
 <target name="pdf" description="Generate PDF via Aspose.PDF for JasperReports.">
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

11. Чтобы запустить демо-версию:
   - Загрузите инструмент ANT с сайта <http://ant.apache.org/bindownload.cgi>.
   - Распакуйте инструмент ANT и настройте переменные среды, как описано в руководстве к инструменту.
   -  Измените текущий каталог на <InstallDir>\demo\hsqldb и выполните следующую командную строку:
      `ant runServer`
12. Откройте новый экземпляр командной строки, измените текущий каталог на <InstallDir>\demo\samples\fonts.ap и выполните следующие команды в командной строке:
13. ant javac — для компиляции исходных файлов Java тестового приложения
14. ant compile – для компиляции дизайна отчета XML и создания файла .jasper.
15. ant fill – для заполнения скомпилированного отчета данными и создания файла .jrprint.
16. `ant aspose_pdf` — для создания PDF-файла с использованием Aspose.PDF for JasperReports.
17. Откройте полученный PDF-файл (**FontsReport.pdf**) из папки <InstallDir>\demo\samples\fonts.ap\build\reports\.

{{% /alert %}}
