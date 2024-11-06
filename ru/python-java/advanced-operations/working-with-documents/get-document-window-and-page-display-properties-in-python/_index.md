---
title: Получение свойств окна документа и отображения страницы в Python
type: docs
weight: 30
url: ru/python-java/get-document-window-and-page-display-properties-in-python/
---

<ins>Чтобы получить свойства окна документа и отображения страницы PDF-документа с использованием **Aspose.PDF Java for Python**, просто вызовите класс **GetDocumentWindow**.

**Код на Python**
```

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# Получить различные свойства документа
# Положение окна документа - по умолчанию: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Преобладающий порядок чтения; определяет положение страницы
# при отображении рядом - по умолчанию: L2R
print "Direction :- " + str(doc.getDirection())

# Должна ли строка заголовка окна отображать заголовок документа.
# Если false, строка заголовка отображает имя файла PDF - по умолчанию: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# Следует ли изменять размер окна документа, чтобы он соответствовал размеру
# первой отображаемой страницы - по умолчанию: false

print "FitWindow :- " + str(doc.getFitWindow())

# Скрыть ли строку меню в приложении просмотра - По умолчанию: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Скрыть ли панель инструментов в приложении просмотра - По умолчанию: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Скрыть ли элементы интерфейса, такие как полосы прокрутки,
# оставляя только содержимое страниц - По умолчанию: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# Разметка страницы, то есть одна страница, одна колонка
print "PageLayout :-" + str(doc.getPageLayout())

# Как документ должен отображаться при открытии.
print "pageMode :-" + str(doc.getPageMode())
```

**Скачать работающий код**

Скачайте **Get Document Window and Page Display Properties (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)