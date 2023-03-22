if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:public_app", reload=True)
