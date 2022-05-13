import IPConsolidator as combiner

def __init__():
    try:
        obj = combiner.IPConsolidator().invoke_job()
        # print(combiner.invoke_job())
        print(obj)
    except Exception as e:
        print("An error has occured... Please make sure arguments are passed properly")
        print(e)

if __name__ == "__main__":
    __init__()