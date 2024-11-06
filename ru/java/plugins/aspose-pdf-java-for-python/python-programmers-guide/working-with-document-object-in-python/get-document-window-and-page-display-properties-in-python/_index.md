---
title: Получение Свойств Окна Документа и Отображения Страницы в Python
type: docs
weight: 30
url: ru/java/get-document-window-and-page-display-properties-in-python/
lastmod: "2021-06-05"
---

Чтобы получить свойства окна документа и отображения страницы PDF-документа, используя **Aspose.PDF Java для Python**, просто вызовите класс **GetDocumentWindow**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Получить разные свойства документа
# Положение окна документа - По умолчанию: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Основной порядок чтения; определяет положение страницы
# при отображении рядом - По умолчанию: L2R
print "Direction :- " + str(doc.getDirection())

# Должна ли строка заголовка окна отображать заголовок документа.
# Если false, строка заголовка отображает имя файла PDF - По умолчанию: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# Следует ли изменять размер окна документа для соответствия размеру
# первой отображаемой страницы - По умолчанию: false
print "FitWindow :- " + str(doc.getFitWindow())

# Следует ли скрыть строку меню приложения просмотра - По умолчанию: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Следует ли скрыть панель инструментов приложения просмотра - По умолчанию: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Следует ли скрыть элементы интерфейса, такие как полосы прокрутки,
# оставив только содержимое страницы - По умолчанию: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# Макет страницы, т.е. одна страница, одна колонка
print "PageLayout :-" + str(doc.getPageLayout())

# Как документ должен отображаться при открытии.
print "pageMode :-" + str(doc.getPageMode())
```


**Скачать исполняемый код**

Скачайте **Получить свойства окна документа и отображения страницы (Aspose.PDF)** с любого из перечисленных ниже социально-кодирующих сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)