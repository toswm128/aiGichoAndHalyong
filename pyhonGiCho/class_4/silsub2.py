def printMenu():
    print("\n=== 할 일 관리 프로그램 ===")
    print("1. 할 일 추가")
    print("2. 할 일 조회")
    print("3. 완료 상태 변경")
    print("4. 할 일 삭제")
    print("0. 종료")
    return input("선택: ")


def addTodo(todos):
    text = input("할 일: ").strip()

    if text == "":
        print("할 일을 입력해야합니다.")
        return
    todo = {"text": text, "done": False}
    todos.append({"id": len(todos), **todo})


def printTodo(todos):
    if (len(todos) == 0):
        print("할 일이 없습니디다.")
        return

    print("\n--- 할 일 목록 ---")
    for key, todo in enumerate(todos, start=1):
        status = ""
        if todo["done"]:
            status = "완료"
        else:
            status = "미완료"

        print(f"{key}. {todo["text"]} [{status}]")
    print(
        f"\n완료된 할 일: {len(list(filter(lambda todo: todo["done"] is True, todos)))} 미완료한 할 일 개수: {len(list(filter(lambda todo: todo["done"] is False, todos)))} 총 할 일 갯수: {len(todos)}")


def completeTodo(todos):
    if len(todos) == 0:
        print("변경할 일이 없습니다.")
        return

    printTodo(todos)
    id = int(input("변경할 번호: "))

    if 1 <= id <= len(todos):
        todos[id-1]["done"] = not todos[id-1]["done"]
        print("변경 처리되었습니다.")
    else:
        print("존재하지 않는 번호입니다.")


def deleteTodo(todos):
    if len(todos) == 0:
        print("삭제 할 일이 없습니다.")
        return

    printTodo(todos)
    id = int(input("삭제할 번호: "))

    if 1 <= id <= len(todos):
        todos.pop(id-1)
        print("삭제 처리되었습니다.")
    else:
        print("존재하지 않는 번호입니다.")


def selectMenu(menu, todos):
    match menu:
        case "1":
            addTodo(todos)
        case "2":
            printTodo(todos)
        case "3":
            completeTodo(todos)
        case "4":
            deleteTodo(todos)
        case "0":
            return 0
        case _:
            print("존재하지 않는 메뉴입니다.")


def startTodo():
    todos = [{"id": 0, "text": "할것", "done": False}]
    while True:
        if selectMenu(printMenu(), todos) == 0:
            break


def init():
    startTodo()


init()
