import { useEffect, useRef } from 'react';

interface WebSocketMessage {
    event: string;
    data: any;
}

export const useWebSocket = (url: string, handlers: {
    onMessage: (data: any) => void;
    onError?: (error: Event) => void;
}) => {
    const ws = useRef<WebSocket | null>(null);

    useEffect(() => {
        ws.current = new WebSocket(url);
        
        ws.current.onmessage = (event) => {
            try {
                const message: WebSocketMessage = JSON.parse(event.data);
                handlers.onMessage(message);
            } catch (error) {
                console.error('WebSocket message error:', error);
            }
        };

        ws.current.onerror = (error) => {
            handlers.onError?.(error);
        };

        return () => {
            ws.current?.close();
        };
    }, [url]);

    const send = (data: WebSocketMessage) => {
        if (ws.current?.readyState === WebSocket.OPEN) {
            ws.current.send(JSON.stringify(data));
        }
    };

    return { send };
};
