from django.shortcuts import render

# Create your views here.
def linkedlist(request):
    return render(request, 'pages/learn/datastructures/linkedlist.html')

def stack(request):
    return render(request, 'pages/learn/datastructures/stack.html')

def queue(request):
    return render(request, 'pages/learn/datastructures/queue.html')
def heap(request):
    return render(request, 'pages/learn/datastructures/heap.html')
def hashing(request):
    return render(request, 'pages/learn/datastructures/hashing.html')
def graph(request):
    return render(request, 'pages/learn/datastructures/graph.html')


def linearsearch(request):
    return render(request, 'pages/learn/searching/linearsearch.html')
def binarysearch(request):
    return render(request, 'pages/learn/searching/binarysearch.html')


def bubblesort(request):
    return render(request, 'pages/learn/sorting/bubblesort.html')
def bucketsort(request):
    return render(request, 'pages/learn/sorting/bucketsort.html')
def countingsort(request):
    return render(request, 'pages/learn/sorting/countingsort.html')
def heapsort(request):
    return render(request, 'pages/learn/sorting/heapsort.html')
def insertionsort(request):
    return render(request, 'pages/learn/sorting/insertionsort.html')
def mergesort(request):
    return render(request, 'pages/learn/sorting/mergesort.html')
def quicksort(request):
    return render(request, 'pages/learn/sorting/quicksort.html')
def radixsort(request):
    return render(request, 'pages/learn/sorting/radixsort.html')
def selectionsort(request):
    return render(request, 'pages/learn/sorting/selectionsort.html')


def avltree(request):
    return render(request, 'pages/learn/trees/avltree.html')
def binarytree(request):
    return render(request, 'pages/learn/trees/binarytree.html')
def binarysearchtree(request):
    return render(request, 'pages/learn/trees/binarysearchtree.html')
def bplustree(request):
    return render(request, 'pages/learn/trees/bplustree.html')
def redblacktree(request):
    return render(request, 'pages/learn/trees/redblacktree.html')
def tries(request):
    return render(request, 'pages/learn/trees/tries.html')


def bfs(request):
    return render(request, 'pages/learn/graphs/bfs.html')
def dfs(request):
    return render(request, 'pages/learn/graphs/dfs.html')
def mst(request):
    return render(request, 'pages/learn/graphs/mst.html')
def dijkstra(request):
    return render(request, 'pages/learn/graphs/dijkstra.html')
def bellman_ford(request):
    return render(request, 'pages/learn/graphs/dfs.html')
def floyd_warshall(request):
    return render(request, 'pages/learn/graphs/floyd_warshall.html')

