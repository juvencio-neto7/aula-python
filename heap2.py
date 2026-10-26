import heapq
tarefas = []
heapq.heappush(tarefas, (1, 'Urgente'))
heapq.heappush(tarefas, (3, 'Normal'))
heapq.heappush(tarefas, (2, 'Importante'))

print(heapq.heappop(tarefas))