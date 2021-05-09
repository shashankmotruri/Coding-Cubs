from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
   path('linkedlist/',views.linkedlist,name='linkedlist'),
   path('stack/',views.stack,name='stack'),
   path('queue/',views.queue,name='queue'),
   path('heap/',views.heap,name='heap'),
   path('hashing/',views.hashing,name='hashing'),
   path('graph/',views.graph,name='graph'),

   path('linearsearch/',views.linearsearch,name='linearsearch'),
   path('binarysearch/',views.binarysearch,name='binarysearch'),

   path('bubblesort/',views.bubblesort,name='bubblesort'),
   path('bucketsort/',views.bucketsort,name='bucketsort'),
   path('countingsort/',views.countingsort,name='countingsort'),
   path('heapsort/',views.heapsort,name='heapsort'),
   path('insertionsort/',views.insertionsort,name='insertionsort'),
   path('mergesort/',views.mergesort,name='mergesort'),
   path('quicksort/',views.quicksort,name='quicksort'),
   path('radixsort/',views.radixsort,name='radixsort'),
   path('selectionsort/',views.selectionsort,name='selectionsort'),
 
   path('binarytree/',views.binarytree,name='binarytree'),
   path('binarysearchtree/',views.binarysearchtree,name='binarysearchtree'),
   path('bplustree/',views.bplustree,name='bplustree'),
   path('redblacktree/',views.redblacktree,name='redblacktree'),
   path('avltree/',views.avltree,name='avltree'),
   path('tries/',views.tries,name='tries'),

   path('bfs/',views.bfs,name='bfs'),
   path('dfs/',views.dfs,name='dfs'),
   path('mst/',views.mst,name='mst'),
   path('dijkstra/',views.dijkstra,name='dijkstra'),
   path('bellman_ford/',views.bellman_ford,name='bellman_ford'),
   path('floyd_warshall/',views.floyd_warshall,name='floyd_warshall'),
   
]