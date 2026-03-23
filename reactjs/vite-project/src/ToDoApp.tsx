import { useState, type ChangeEvent } from "react";

function ToDoList() {

    const [tasks, setTasks] = useState<string[]>([]);
    const [textvalue, setTextValue] = useState<string>("");

    const handletextvalue = (event: ChangeEvent<HTMLInputElement>) => {
        setTextValue(event.target.value);
    };

    const addtask = () => {
        if (textvalue.trim() !== "") {
            setTasks((prev: string[]) => [...prev, textvalue]);
            setTextValue("");
        }
    };

    const deletetask = (index: number) => {
        setTasks(prev => prev.filter((_, i) => i !== index));
    };

    const moveup = (index: number) => {
        if (index > 0) {
            setTasks(prevTasks => {
                const updatetask = [...prevTasks];
                [updatetask[index], updatetask[index - 1]] =
                [updatetask[index - 1], updatetask[index]];
                return updatetask;
            });
        }
    };

    const movedown = (index: number) => {
        if (index < tasks.length - 1) {
            setTasks(prevTasks => {
                const updatetask = [...prevTasks];
                [updatetask[index], updatetask[index + 1]] =
                [updatetask[index + 1], updatetask[index]];
                return updatetask;
            });
        }
    };

    return (
        <>
            <div className="p-5 border-2 border-b-blue-200 ">
                <h1 className="font-extrabold font-mono text-4xl mb-4">
                    To-Do-List
                </h1>

                <ol>
                    {tasks.map((task, index) => (
                        <li
                            key={index}
                            className="font-mono font-extrabold text-2xl flex items-center gap-2 mb-2 border-2 w-[70%] px-10 cursor-pointer bg-green-100 hover:scale-x-105"
                        >
                            {task}

                            <button
                                className="border-2 p-1 w-fit border-red-400 ml-auto active:scale-y-50 cursor-grab"
                                onClick={() => deletetask(index)}
                            >
                                🚮
                            </button>

                            <button
                                className="border-2 p-1 w-fit border-amber-400 active:scale-50 transition-transform duration-150 cursor-grab"
                                onClick={() => moveup(index)}
                            >
                                👆
                            </button>

                            <button
                                className="border-2 p-1 w-fit border-amber-400 active:scale-x-150 transition-transform duration-150 cursor-grab"
                                onClick={() => movedown(index)}
                            >
                                👇
                            </button>
                        </li>
                    ))}
                </ol>

                <input
                    type="text"
                    value={textvalue}
                    onChange={handletextvalue}
                    className="border-2 border-gray-300 rounded-lg p-2 w-[40%]"
                    placeholder="Enter a task to add"
                />

                <button
                    onClick={addtask}
                    className="ml-2 border-2 border-blue-500 bg-blue-500 text-white px-4 py-2 rounded-lg active:scale-x-50 cursor-grab"
                >
                    Add Task
                </button>
            </div>
        </>
    );
}

export default ToDoList;