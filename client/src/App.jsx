import { useState, useEffect, useRef } from 'react';
import axios from 'axios';

function App() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [loadingText, setLoadingText] = useState('');

    // Ref for the chat container
    const chatContainerRef = useRef(null);

    const formatText = (text) => {
        return text.split('\n').map((line, index) => (
            <span key={index}>
                {line}
                <br />
            </span>
        ));
    };

    const handleSendMessage = async () => {
        if (!input.trim()) return;

        const userMessage = { sender: 'human', content: input };
        setMessages((prev) => [...prev, userMessage]);
        setInput('');
        setIsLoading(true);

        try {
            const payload = {
                messages: [
                    ...messages.map((msg) => ({
                        content: msg.text || msg.content,
                        sender: msg.sender.toLowerCase(),
                    })),
                    { content: input, sender: 'human' },
                ],
            };

            console.log('Request payload:', payload);

            setLoadingText('Thinking...');

            const response = await axios.post(
                'http://localhost:8000/chat/get-stationmaster-response',
                payload
            );

            console.log('Response:', response.data);

            setMessages((prev) => [
                ...prev,
                { sender: 'stationmaster', text: response.data.data.output },
            ]);
        } catch (error) {
            console.error('Error fetching response:', error);
            setMessages((prev) => [
                ...prev,
                { sender: 'stationmaster', text: 'Failed to fetch response.' },
            ]);
        } finally {
            setIsLoading(false);
            setLoadingText('');
        }
    };

    useEffect(() => {
        if (!isLoading) return;

        const interval = setInterval(() => {
            setLoadingText((prev) => {
                if (prev === 'Thinking...') return 'Searching...';
                if (prev === 'Searching...') return 'Generating...';
                return 'Thinking...';
            });
        }, 3000);

        return () => clearInterval(interval);
    }, [isLoading]);

    // Scroll to the latest message whenever messages change
    useEffect(() => {
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop =
                chatContainerRef.current.scrollHeight;
        }
    }, [messages, isLoading]);

    return (
        <div className="flex h-screen bg-gray-900 text-gray-300 font-sans">
            {/* Left Pane: Image (Hidden on small screens) */}
            <div className="hidden md:block w-1/3 p-4">
                <img
                    src="/stationmaster.webp"
                    alt="StationMaster"
                    className="w-full h-full object-cover rounded-lg shadow-md"
                />
            </div>

            {/* Right Pane: Chat */}
            <div className="w-full md:w-2/3 p-4 flex flex-col">
                {/* Chat Messages Container */}
                <div
                    ref={chatContainerRef}
                    className="flex-1 overflow-y-auto mb-4 space-y-4"
                >
                    {messages.map((msg, index) => (
                        <div
                            key={index}
                            className={`p-3 rounded-lg ${
                                msg.sender === 'human'
                                    ? 'bg-blue-600 text-white self-end'
                                    : 'bg-gray-700 text-gray-300 self-start'
                            }`}
                        >
                            <div className="font-bold mb-1">
                                {msg.sender === 'human'
                                    ? 'You'
                                    : 'StationMaster'}
                            </div>
                            <div>{formatText(msg.text || msg.content)}</div>
                        </div>
                    ))}
                    {isLoading && (
                        <div className="p-3 rounded-lg bg-gray-700 text-gray-300 animate-pulse self-start">
                            <div className="font-bold mb-1">StationMaster</div>
                            <div>{loadingText}</div>
                        </div>
                    )}
                </div>

                {/* Input Area */}
                <div className="flex">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyPress={(e) =>
                            e.key === 'Enter' && handleSendMessage()
                        }
                        className="flex-1 p-3 bg-gray-800 text-gray-300 border border-gray-600 rounded-l-lg text-lg focus:outline-none focus:ring focus:ring-blue-500"
                        placeholder="Type your message..."
                        disabled={isLoading}
                    />
                    <button
                        onClick={handleSendMessage}
                        className="p-3 bg-blue-600 text-white rounded-r-lg text-lg hover:bg-blue-700 disabled:bg-gray-400"
                        disabled={isLoading}
                    >
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
}

export default App;
