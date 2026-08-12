---
title: Как использовать Aspose.PDF для автономных демонстраций JasperReports
linktitle: Как использовать Aspose.PDF для автономных демонстраций JasperReports
type: docs
weight: 10
url: /ru/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: Изучите офлайн-демоверсии Aspose.PDF для JasperReports. Изучите практические реализации и функции на практике.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF для JasperReports включает ряд демонстрационных проектов, которые помогут вам начать экспортировать отчеты в форматы PDF из вашего приложения. Демо-версии представляют собой стандартные демо-версии JasperReports, которые были изменены, чтобы продемонстрировать, как использовать новые средства экспорта.

{{% /alert %}}

## Запустите Aspose.PDF для демонстраций JasperReports

Чтобы запустить демонстрационный файл Aspose.PDF для JasperReports:

{{% alert color="primary" %}}

1. Загрузите JasperReports с сайта <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.. Обязательно загрузите весь заархивированный проект с исходным кодом и демонстрациями, а не только один JAR-файл.
2. Распакуйте заархивированный проект в какое-нибудь место на жестком диске, например C:\..
3. Скопируйте все демонстрационные папки из папки \demo в **Aspose.PDF.JasperReports.zip** в ```<InstallDir>```\jasperreports\demo\samples, где ```<InstallDir>``` — это каталог, в который вы распаковали JasperReports. Этот шаг является обязательным, поскольку демонстрационные сценарии сборки используют структуру папок JasperReports, в противном случае вам придется изменить сценарии сборки.
4. Скопируйте файл **aspose.pdf.jasperreports.jar** из папки \lib в **Aspose.PDF.JasperReports.zip** в ```<InstallDir>```\jasperreports\lib.
5. Загрузите инструмент ANT с сайта <http://ant.apache.org/bindownload.cgi>..
6. Распакуйте инструмент ANT и настройте переменные среды, как описано в руководстве к инструменту.
7. Перейдите в каталог ```<InstallDir>```\demo\hsqldb и выполните следующую команду:
   ant runServer
8. Откройте новый экземпляр командной строки и измените текущий каталог на одну из демонстрационных версий Aspose.PDF for JasperReports, например ```<InstallDir>```\demo\samples\charts.ap.
9. Выполните следующие команды в командной строке:
10. Выполните команду `ant javac`, чтобы скомпилировать исходные файлы Java тестового приложения.
11. Выполните команду `ant compile`, чтобы скомпилировать XML-дизайн отчета и создать файл `.jasper`.
12. Выполните команду `ant fill`, чтобы заполнить скомпилированный отчет данными и создать файл `.jrprint`.
13. Выполните следующую команду в командной строке:
   `ant pdf` — для создания PDF-файла из демонстрационного отчета.
14. Откройте один из полученных документов для просмотра, например ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf в Adobe Reader или другом приложении.

{{% /alert %}}


