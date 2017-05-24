#coding:utf-8
#Textmining:test for Textmining using
#Lucas
#2017/5/24
import textmining
import os

def termdocumentmatrix_example():
    # 创建短文本
    doc1 = 'John and Bob are brothers.' 
    doc2 = 'John went to the store. The store was closed.'
    doc3 = 'Bob went to the store too.'
    # 初始化类生成短文本矩阵，只能处理英文词条
    tdm = textmining.TermDocumentMatrix()
    # 添加文本
    tdm.add_doc(doc1)
    tdm.add_doc(doc2)
    tdm.add_doc(doc3)

    # 将矩阵写入CSV文件，"cutoff = 1"表示出现在"1"个及以上的文本中的单词将会被输出，默认的cutoff＝2
    # 此处需要每个单词都显示出来，所以设值为1，否则只会显示出现在至少两个文本中的单词
    tdm.write_csv('matrix.csv', cutoff=1)

    # 输出
    print '\ntermdocumentmatrix_example 1\n'
    for row in tdm.rows(cutoff=1):
        print row

def splitby_example():
    # The splitby function in the textmining package is very useful.
    # 根据用户定义的划分函数，允许对长文本划分为短文本或词条进行灵活的划分

    # First let's use the default split function which splits a sequence
    # of lines into groups corresponding to paragraphs. The function
    # defines a paragraph boundary to lie between a non-blank line and
    # blank line.
    # 使用默认的划分函数
    text = """

    Hello there
    how are you today?

    I hope you
    are doing well.

    Thanks for using the textmining module!


    """
    lines = text.splitlines()
    print '\nsplitby_example 1\n'
    for paragraph in textmining.splitby(lines):
        # paragraph is a list of lines.
        # Notice that the last paragraph will just contain
        # lines of spaces as there is no text in it.
        print paragraph
    
    #使用通用的划分函数处理更加复杂的文本，删除无意义的空格得出更加清晰的词条
    text = """

    Document One:
    -------------

    First line of Document One
    Second line of Document One

    Third line of Document One

    Document Two:
    -------------

    First line of Document Two

    Second line of Document Two
    Document Three:
    ---------------
    First line of Document Three


    """

    # 为文本边界定义函数
    def document_boundary(line1, line2):
        return line2.strip().startswith('Document')

    # 文本循环
    lines = text.splitlines()
    print '\nsplitby_example 2\n'
    for document in textmining.splitby(lines, document_boundary):
        # 如果第一行不符合文本结构则跳过
        if not document[0].strip().startswith('Document'):
            continue
        # 删除空格，得出新的词条
        clean_lines = [line.strip() for line in document if line.strip()]
        # 输出
        print '\n'.join(clean_lines)
        print

def dictionary_example():
    # 输出字典中词频最高的十个单词
    freq_word = [(counts[0][0], word) for (word, counts) in \
      textmining.dictionary.items()]
    freq_word.sort(reverse=True)
    print '\ndictionary_example 1\n'
    for freq, word in freq_word[:10]:
        print word, freq

    #同一个词可以用英文的许多不同的语境来使用。 
    #textmining模块中的字典包含给定字的这些部分语音的相对频率。
    #关于部分语音代码的说明在doc / poscodes.html中。这里是“开放”一词的词性频率。
    print '\ndictionary_example 2\n'
    print textmining.dictionary['test']


def names_example():
    # textmining模块包含三个关于名字的字典
    # 名字是键，值是该名字在US人口普查中的频率百分比值

    #找到一些男性名字的相关频率
    print '\nnames_example 1\n'
    for name in ('john', 'tom', 'william', 'boris'):
        freq = textmining.names_male[name]
        print name, freq

    #找出十大最普遍的姓
    f = [(freq, name) for (name, freq) in textmining.names_last.items()]
    f.sort(reverse=True)
    print '\nnames_example 2\n'
    for freq, name in f[:10]:
        print name, freq

def bigram_collocations_example():
    # 使用统计的方法，找出《夏洛克福尔摩斯的冒险中》的十大最重要的二词短语
    example_dir = os.path.dirname(__file__)
    sample_text_file = os.path.join(example_dir, 'holmes.txt')
    text = open(sample_text_file).read()
    words = textmining.simple_tokenize(text)
    bigrams = textmining.bigram_collocations(words)
    print '\nbigram_collocations_example 1\n'
    for bigram in bigrams[:10]:
        print ' '.join(bigram)

termdocumentmatrix_example()
splitby_example()
dictionary_example()
names_example()
bigram_collocations_example()


