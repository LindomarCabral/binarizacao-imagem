# 🖼️ Processamento de Imagens - Binarização com Python

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.19%2B-orange)](https://numpy.org/)

Um projeto acadêmico avançado que implementa **algoritmos próprios** para processamento de imagens, demonstrando domínio em visão computacional e programação Python.

## 🎯 Objetivo do Projeto

Implementar do zero (sem usar funções prontas de bibliotecas) o processo completo de:
- **Conversão** de imagens coloridas para tons de cinza
- **Binarização** de imagens em preto e branco

## ✨ Destaques Técnicos

🚫 **Não utiliza funções prontas** do OpenCV para conversões
🧠 **Implementação manual** dos algoritmos fundamentais
📊 **Controle total** sobre o processo de binarização
🎨 **Resultados visuais** de alta qualidade

## 🛠️ Tecnologias Utilizadas

- **Python 3.6+**
- **OpenCV** (apenas para I/O de imagens)
- **NumPy** (para manipulação de arrays)

## 📁 Estrutura do Projeto

```
binarizacao-imagem/
├── binarize.py          # Script principal
├── jaguar.png           # Imagem de exemplo
├── jaguar_cinza.jpg     # Resultado: tons de cinza
├── jaguar_binaria.jpg   # Resultado: preto e branco
└── README.md           # Este arquivo
```

## 🚀 Como Usar

### 1. Clone o repositório
```bash
git clone https://github.com/LindomarCabral/binarizacao-imagem.git
cd binarizacao-imagem
```

### 2. Instale as dependências
```bash
pip install opencv-python numpy
```

### 3. Execute o projeto
```bash
python binarize.py
```

### 4. Resultados
O script irá exibir três janelas:
- 🎨 **Imagem Original Colorida**
- ⚫ **Imagem em Tons de Cinza** (nossa implementação)
- ⚪ **Imagem Binarizada** (nossa implementação)

## 🔧 Funcionalidades Implementadas

### 1. Conversão RGB para Tons de Cinza
**Nossa implementação:**
```python
def rgb_para_cinza(imagem_colorida):
    # Aplicamos a fórmula de luminância humana:
    # cinza = 0.299*R + 0.587*G + 0.114*B
    # Processamos pixel a pixel manualmente
```

### 2. Binarização por Limiar
**Nossa implementação:**
```python
def binarizar_imagem(imagem, limiar=60):
    # Para cada pixel:
    # - Se intensidade >= limiar → Branco (255)
    # - Se intensidade < limiar → Preto (0)
```

## 📊 Exemplo de Saída

```
Convertendo colorido → tons de cinza...
Binarizando com limiar 60...

Processamento concluído!
✓ Conversão colorido → tons de cinza: FEITA com nossa função
✓ Binarização cinza → preto/branco: FEITA com nossa função
✓ Limiar utilizado: 60
✓ Imagens salvas: jaguar_cinza.jpg, jaguar_binaria.jpg
```

## 🎛️ Personalização

### Ajuste do Limiar de Binarização
No arquivo `binarize.py`, linha 38:
```python
img_binaria = binarizar_imagem(img_cinza, limiar=60)  # Altere este valor
```

**Valores sugeridos:**
- `30-50`: Mais pixels brancos (imagem mais clara)
- `60-80`: Equilibrado 
- `90-120`: Mais pixels pretos (imagem mais escura)

## 📈 Habilidades Demonstradas

### 💻 Programação
- Manipulação avançada de imagens com NumPy
- Processamento pixel a pixel eficiente
- Implementação de algoritmos computacionais

### 🧮 Fundamentos Matemáticos
- Modelo de cores RGB e escala de cinza
- Fórmula de luminância para percepção humana
- Limiarização (thresholding) para binarização

### 🔬 Visão Computacional
- Processamento digital de imagens
- Técnicas de pré-processamento
- Análise e manipulação de histogramas

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como parte do estudo em **Processamento Digital de Imagens**, demonstrando a compreensão fundamental dos algoritmos por trás das funções de bibliotecas populares como OpenCV.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Adicionar novos algoritmos de binarização
- Implementar detecção automática de limiar
- Melhorar a eficiência do código
- Adicionar suporte a mais formatos de imagem

## 📄 Licença

Este projeto é open source e está disponível sob a [MIT License](LICENSE).

---

**Desenvolvido com ❤️ para demonstrar habilidades avançadas em Python e Processamento de Imagens**

*"Não basta saber usar as bibliotecas, é preciso entender os algoritmos por trás delas."*