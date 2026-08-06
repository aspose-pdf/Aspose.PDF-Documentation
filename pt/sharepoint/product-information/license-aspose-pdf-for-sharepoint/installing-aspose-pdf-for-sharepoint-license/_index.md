---
title: Instalando Aspose.PDF para licença do SharePoint
linktitle: Instalando Aspose.PDF para licença do SharePoint
type: docs
weight: 10
url: /pt/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Quando estiver satisfeito com sua avaliação, você poderá adquirir uma licença para PDF SharePoint API e seguir as instruções de instalação para aplicá-la.
---

{{% alert color="primary" %}}

Quando estiver satisfeito com sua avaliação, você poderá [comprar uma licença](https://purchase.aspose.com/buy). Antes de comprar, certifique-se de compreender e concordar com os termos de assinatura da licença.

{{% /alert %}}

{{% alert color="primary" %}}

A licença será enviada para você por e-mail após o pagamento do pedido. A licença é um arquivo .zip que contém um pacote de solução regular do SharePoint.

Este arquivo contém:

- Aspose.PDF.SharePoint.License.wsp

Arquivo do pacote de solução do SharePoint. A licença Aspose.PDF para SharePoint é empacotada como uma solução SharePoint para facilitar a implantação/retração em todo o farm de servidores.

- leia-me.txt

Instruções de instalação da licença. A instalação da licença é realizada no console do servidor por meio de stsadm.exe. As etapas necessárias para instalar a licença são fornecidas abaixo.

**Observação:** Os caminhos foram omitidos para maior clareza. Pode ser necessário adicionar o caminho real para stsadm.exe e/ou arquivo de solução ao executá-los.

1. Execute stsadm para adicionar a solução ao armazenamento de soluções do SharePoint:

stsadm.exe -o addolution -nome do arquivo Aspose.PDF.SharePoint.License.wsp

2. Implante a solução em todos os servidores do farm:

stsadm.exe -o implantsolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Execute trabalhos de timer administrativo para concluir a implantação imediatamente.

stsadm.exe -o execadmsvcjobs

**Observação:** Você receberá um aviso ao executar a etapa de implantação se o serviço de Administração do Windows SharePoint Services não for iniciado. Stsadm.exe depende desse serviço e do Windows SharePoint Timer Service para replicar dados da solução em todo o farm. Se esses serviços não estiverem em execução no farm de servidores, talvez seja necessário implantar a licença em cada servidor.

{{% /alert %}}

