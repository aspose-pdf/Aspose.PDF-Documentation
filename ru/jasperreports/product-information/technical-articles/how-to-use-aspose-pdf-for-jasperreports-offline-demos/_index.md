---
title: How to - use Aspose.Pdf for JasperReports offline demos
type: docs
weight: 10
url: /ru/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports включает в себя ряд демонстрационных проектов, чтобы помочь вам начать экспорт отчетов в PDF форматы из вашего приложения. Демонстрации являются стандартными демонстрациями JasperReports, которые были изменены для демонстрации использования новых экспортеров.

{{% /alert %}}
### **Запуск демонстраций Aspose.PDF для JasperReports**
Чтобы запустить демонстрации Aspose.PDF для JasperReports:

{{% alert color="primary" %}}

1. Загрузите JasperReports с <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Убедитесь, что вы загрузили весь архивированный проект с исходным кодом и демонстрациями, а не только один JAR.
2. Распакуйте архивированный проект в какое-то место на вашем жестком диске, например, в C:\.
3. 1. Скопируйте все папки с демо из папки \demo в **Aspose.PDF.JasperReports.zip** в ```<InstallDir>```\jasperreports\demo\samples, где ```<InstallDir>``` — это расположение, в которое вы распаковали JasperReports. Этот шаг необходим, потому что скрипты сборки демо зависят от структуры папок JasperReports, в противном случае вам придется изменить скрипты сборки.
2. Скопируйте файл **aspose.pdf.jasperreports.jar** из папки \lib в **Aspose.PDF.JasperReports.zip** в ```<InstallDir>```\jasperreports\lib.
3. Загрузите инструмент ANT с <http://ant.apache.org/bindownload.cgi>.
4. Распакуйте инструмент ANT и настройте переменные среды, как описано в руководстве инструмента.
5. Измените текущий каталог на ```<InstallDir>```\demo\hsqldb и выполните следующую командную строку:
   ant runServer
6. Откройте новый экземпляр командной строки и измените текущий каталог на один из демо Aspose.PDF для JasperReports, например ```<InstallDir>```\demo\samples\charts.ap.
7. Выполните следующие команды в командной строке:
8. 
ant javac – для компиляции Java исходных файлов тестового приложения.
11. ant compile – для компиляции XML-дизайна отчета и создания .jasper файла
12. ant fill – для заполнения скомпилированного дизайна отчета данными и создания .jrprint файла
13. Выполните следующую команду в командной строке:
   ant pdf – для создания PDF файла из демо-отчета.
14. Откройте один из полученных документов для просмотра, например ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf в Adobe Reader или другом приложении.

{{% /alert %}}
```