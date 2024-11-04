---
title: How to - Update existing JasperReports demos to use Aspose.Pdf for JasperReports
type: docs
weight: 20
url: /jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF для JasperReports включает ряд демонстрационных проектов, чтобы помочь вам начать экспорт отчетов в PDF. Эти демонстрации основаны на стандартных демонстрациях JasperReports, которые были изменены для демонстрации использования новых экспортеров. Этот учебник проходит через шаги, необходимые для обновления существующих демонстраций JasperReports для использования Aspose.PDF для JasperReports.

{{% /alert %}}
### **Обновление демонстраций для использования Aspose.PDF**

{{% alert color="primary" %}}

Следующие шаги объясняют, как обновить существующие демонстрации для использования расширения экспорта Aspose.PDF для JasperReports вместо использования стандартной функции экспорта PDF JasperReport.
{{% /alert %}}
1. Скачайте JasperReports с <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Убедитесь, что вы скачали весь архивированный проект с исходным кодом и демонстрациями, а не только один JAR. Этот учебник был подготовлен с использованием JasperReports-3.5.2.
2. Распакуйте архивированный проект в любое место на вашем жестком диске, например, C:\.
3. Скопируйте **aspose.pdf.jasperreports.jar** из папки \lib в **Aspose.PDF.JasperReports.zip** в ```<InstallDir>```\jasperreports\lib.
4. Откройте ```<InstallDir>```\jasperreports\demo\samples, (где ```<InstallDir>``` — это место, куда вы распаковали JasperReports) чтобы обновить существующий демо-проект. Если вы выбрали, например, демо шрифтов для использования с Aspose.PDF для JasperReports, создайте его копию, чтобы оригинальный демо-проект остался неизменным. Для целей этого примера мы назвали новую папку **fonts.ap**.
Примечание: демо-проекты будут запускаться из ```<InstallDir>``` \jasperreports\demo\samples, потому что скрипты сборки демо-проектов зависят от структуры папок JasperReports. Если вы измените папку с примерами, вам нужно будет изменить скрипты сборки.
5. Откройте файл **FontsApp.java** из папки src и добавьте ссылку на Aspose.PDF для JasperReports:

   import com.aspose.pdf.jr3_7_0.jasperreports.*;    (Мы используем jr3_7_0, потому что этот учебник был подготовлен с JasperReports 3.5.2.)
6. Добавьте новую строку:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; вместе с существующими переменными в качестве опции экспорта через Aspose.PDF для JasperReports.
7. Найдите сегмент кода else if (TASK_PDF.equals(taskName)) и скопируйте весь сегмент.
8. Вставьте фрагмент кода под тем же сегментом.

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
```java
exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
exporter.exportReport();
System.err.println("Время создания PDF : " + (System.currentTimeMillis() - start));
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
9. Откройте файл **build.xml**.
10. Сделайте копию следующего сегмента и поместите его в тот же файл:

```
<target name="pdf" description="Создание PDF через Aspose.PDF для JasperReports.">
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

11. Чтобы запустить демонстрацию:

   -  Скачайте инструмент ANT с <http://ant.apache.org/bindownload.cgi>.
```
- Распакуйте инструмент ANT и настройте переменные окружения, как описано в руководстве по инструменту.
- Измените текущий каталог на <InstallDir>\demo\hsqldb и выполните следующую команду:
  ant runServer
12. Откройте новый экземпляр командной строки и измените текущий каталог на <InstallDir>\demo\samples\fonts.ap и выполните следующие команды в командной строке:
13. ant javac – для компиляции Java исходных файлов тестового приложения
14. ant compile – для компиляции дизайна XML отчета и создания файла .jasper
15. ant fill – для заполнения скомпилированного дизайна отчета данными и создания файла .jrprint
16. ant aspose_pdf – для создания PDF файла с использованием Aspose.PDF для JasperReports.
17. Откройте полученный PDF (**FontsReport.pdf**) из папки <InstallDir>\demo\samples\fonts.ap\build\reports\.