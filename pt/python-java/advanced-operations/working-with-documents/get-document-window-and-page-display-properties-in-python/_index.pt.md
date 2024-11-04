---
title: Obter Propriedades da Janela do Documento e Exibição de Página em Python
type: docs
weight: 30
url: /python-java/get-document-window-and-page-display-properties-in-python/
---

<ins>Para Obter Propriedades da Janela do Documento e Exibição de Página de um documento PDF usando **Aspose.PDF Java for Python**, basta invocar a classe **GetDocumentWindow**.

**Código Python**
```

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# Obter diferentes propriedades do documento
# Posição da janela do documento - Padrão: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Ordem de leitura predominante; determina a posição da página
# quando exibida lado a lado - Padrão: L2R
print "Direction :- " + str(doc.getDirection())

# Se a barra de título da janela deve exibir o título do documento.
# Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# Se redimensionar a janela do documento para ajustar ao tamanho da
# primeira página exibida - Padrão: false

print "FitWindow :- " + str(doc.getFitWindow())

# Se deve ocultar a barra de menu do aplicativo visualizador - Padrão: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Se deve ocultar elementos da interface do usuário como barras de rolagem
# deixando apenas o conteúdo da página exibido - Padrão: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# O modo de página do documento. Como exibir o documento ao sair do modo de tela cheia.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# O layout da página, ou seja, página única, uma coluna
print "PageLayout :-" + str(doc.getPageLayout())

# Como o documento deve ser exibido quando aberto.
print "pageMode :-" + str(doc.getPageMode())


**Baixar Código em Execução**

Baixar **Obter Propriedades de Janela e Exibição de Página do Documento (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)